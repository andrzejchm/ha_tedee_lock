import asyncio
import logging
from typing import Any
from typing import cast
from typing import Optional

from custom_components.ha_tedee_lock.model.devices.device import DeviceType
from homeassistant.components.lock import LockEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import TedeeUpdateCoordinator, device_from_dict
from .const import CONF_DEVICE_INFO
from .const import CONF_DEVICE_TYPE
from .const import DOMAIN
from .model.devices.lock import Lock
from .model.devices.lock import LockState
from .model.states.device_state_lock import DeviceStateLock

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
        hass: HomeAssistant,
        entry: ConfigEntry,
        async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Tedee locks."""
    device_dict: dict = entry.data[CONF_DEVICE_INFO]
    device_type = DeviceType(entry.data[CONF_DEVICE_TYPE])
    coordinator = hass.data[DOMAIN][entry.entry_id]
    device = device_from_dict(device_dict, device_type=device_type)
    if device_type == DeviceType.LOCK:
        async_add_entities(
            [
                TedeeLock(
                    lock=cast(Lock, device),
                    coordinator=coordinator,
                    config_entry=entry,
                )
            ]
        )


class TedeeLock(CoordinatorEntity, LockEntity):
    def __init__(
            self,
            config_entry: ConfigEntry,
            lock: Lock,
            coordinator: TedeeUpdateCoordinator,
    ) -> None:
        super().__init__(coordinator=coordinator)
        self._api = coordinator.api
        self._attr_unique_id = f"tedee-lock-{lock.name}-{lock.id}"
        self._attr_name = lock.name
        self._config_entry = config_entry
        self._lock = lock

    async def async_lock(self, **kwargs: Any) -> None:
        await self._api.async_operation_lock(self._lock.id)
        self._lock_state().lock_properties.state = LockState.Locking
        self.async_write_ha_state()
        self.hass.async_create_task(self._async_delayed_state_refresh(delay_seconds=4))

    async def async_unlock(self, **kwargs: Any) -> None:
        await self._api.async_operation_unlock(self._lock.id)
        self._lock_state().lock_properties.state = LockState.Unlocking
        self.async_write_ha_state()
        self.hass.async_create_task(self._async_delayed_state_refresh(delay_seconds=4))

    @property
    def is_locked(self) -> Optional[bool]:
        return self._lock_state().lock_properties.state == LockState.Locked

    @property
    def is_locking(self) -> Optional[bool]:
        return self._lock_state().lock_properties.state == LockState.Locking

    @property
    def is_unlocking(self) -> Optional[bool]:
        return self._lock_state().lock_properties.state == LockState.Unlocking

    @property
    def is_jammed(self) -> Optional[bool]:
        return self._lock_state().lock_properties.state in [
            LockState.Calibrating,
            LockState.Unknown,
            LockState.Uncalibrated,
        ]

    def _lock_state(self) -> Optional[DeviceStateLock]:
        return self.coordinator.data[self._lock.data_key]

    async def _async_delayed_state_refresh(self, delay_seconds: float = 0.0):
        await asyncio.sleep(delay=delay_seconds)
        await self.coordinator.async_refresh()
