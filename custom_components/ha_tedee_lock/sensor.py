from typing import Optional

from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorEntityDescription, \
    BinarySensorDeviceClass
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass, SensorEntityDescription
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
            LockBatteryLevelSensor(
                lock=Lock.from_dict(device_dict),
                coordinator=coordinator,
            ),
        ])
        pass


class LockBatteryLevelSensor(CoordinatorEntity, SensorEntity):

    def __init__(
            self,
            lock: Lock,
            coordinator: DataUpdateCoordinator,
    ):
        super().__init__(coordinator)
        self._lock = lock
        self.entity_description = SensorEntityDescription(
            key="lock_battery_level",
            state_class=SensorStateClass.MEASUREMENT,
            device_class=SensorDeviceClass.BATTERY,
        )
        self._attr_unique_id = f"tedee-lock-{lock.name}-{lock.id}-lock-battery-level"
        self._attr_name = f"{lock.name} lock battery level"

    @property
    def native_value(self) -> int:
        return self._lock_state().lock_properties.battery_level

    def _lock_state(self) -> Optional[DeviceStateLock]:
        return self.coordinator.data[self._lock.data_key]
