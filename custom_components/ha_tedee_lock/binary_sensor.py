from typing import Optional

from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorEntityDescription, \
    BinarySensorDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator

from .const import CONF_DEVICE_INFO, CONF_DEVICE_TYPE
from .const import DOMAIN
from .model.device_type import DeviceType
from .model.devices.lock import Lock
from .model.states.device_state_lock import DeviceStateLock


async def async_setup_entry(
        hass: HomeAssistant,
        entry: ConfigEntry,
        async_add_entities: AddEntitiesCallback,
) -> None:
    device_dict: dict = entry.data[CONF_DEVICE_INFO]
    device_type = DeviceType(entry.data[CONF_DEVICE_TYPE])
    coordinator = hass.data[DOMAIN][entry.entry_id]
    if device_type == DeviceType.LOCK:
        async_add_entities([
            LockIsChargingBinarySensor(
                lock=Lock.from_dict(device_dict),
                coordinator=coordinator,
            )
        ])
        pass


class LockIsChargingBinarySensor(CoordinatorEntity, BinarySensorEntity):

    def __init__(
            self,
            lock: Lock,
            coordinator: DataUpdateCoordinator,
    ):
        super().__init__(coordinator)
        self._lock = lock
        self.entity_description = BinarySensorEntityDescription(
            key="lock_is_charging",
            device_class=BinarySensorDeviceClass.BATTERY_CHARGING,
        )
        self._attr_unique_id = f"tedee-lock-{lock.name}-{lock.id}-is-charging"
        self._attr_name = f"{lock.name} lock is charging"

    @property
    def is_on(self) -> Optional[bool]:
        return self._lock_state().lock_properties.is_charging

    def _lock_state(self) -> Optional[DeviceStateLock]:
        return self.coordinator.data[self._lock.data_key]
