import logging
from datetime import timedelta
from typing import Tuple

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from . import TedeeLockApiClient
from .const import DOMAIN
from .model.states.device_state import DeviceState

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=30)


class TedeeUpdateCoordinator(DataUpdateCoordinator[dict[int, DeviceState]]):
    def __init__(
            self,
            hass: HomeAssistant,
            api: TedeeLockApiClient,
    ):
        """Initialize my coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            # Name of the data. For logging purposes.
            name=DOMAIN,
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=SCAN_INTERVAL,
        )
        self.data: dict[Tuple[str, int], DeviceState] = {}
        self.api = api

    async def _async_update_data(self) -> dict[Tuple[str, int], DeviceState]:
        data: dict[Tuple[str, int], DeviceState] = {}
        states = await self.api.async_get_devices_states()
        for state in states:
            data[state.data_key] = state

        return data
