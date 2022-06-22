"""Sample API Client."""
import logging
from typing import List

import aiohttp
from homeassistant.core import HomeAssistant

from .const import API_BASE_URL
from .model.devices.bridge import Bridge
from .model.devices.device import Device
from .model.devices.keypad import Keypad
from .model.devices.lock import Lock
from .model.responses.my_bridge_response import MyBridgeResponse
from .model.responses.my_keypad_response import MyKeypadResponse
from .model.responses.my_lock_response import MyLockResponse
from .model.responses.my_lock_sync_response import MyLockSyncResponse
from .model.responses.operation_response import OperationResponse
from .model.states.device_state import DeviceState
from .model.states.device_state_lock import (
    DeviceStateLock,
)

TIMEOUT = 10

_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class TedeeLockApiClient:
    """Api client for Tedee Lock"""

    def __init__(
            self,
            access_token: str,
            session: aiohttp.ClientSession,
            hass: HomeAssistant,
    ) -> None:
        """Sample API Client."""
        self._access_token = access_token
        self._session = session
        self._hass = hass

    async def async_get_devices_info(self) -> List[Device]:
        locks = await self.async_get_locks()
        # bridges = await self.async_get_bridges() TODO enable this when setting up bridges makes sense
        # keypads = await self.async_get_keypads() TODO enable this when setting up keypads makes sense
        return [
            *locks,
            # *bridges,
            # *keypads,
        ]

    async def async_get_devices_states(self) -> List[DeviceState]:
        """Returns all devices' states (locks for now, but in the future might return Keypad if the API supports it)"""
        locks = await self.async_get_locks_states()
        return [
            *locks,
        ]

    async def async_get_locks(self) -> List[Lock]:
        """Returns all locks' device infos"""
        response = await self._session.get(
            f"{API_BASE_URL}/api/v1.25/my/lock",
            headers={**HEADERS, "Authorization": f"PersonalKey {self._access_token}"},
        )
        json = await response.json()
        result = MyLockResponse.from_dict(json)
        return result.result

    async def async_get_locks_states(self) -> List[DeviceStateLock]:
        """Returns all locks' states"""
        response = await self._session.get(
            f"{API_BASE_URL}/api/v1.25/my/lock/sync",
            headers={
                **HEADERS,
                "Authorization": f"PersonalKey {self._access_token}",
            },
        )
        json = await response.json()
        result = MyLockSyncResponse.from_dict(json)
        return result.result

    async def async_get_bridges(self) -> List[Bridge]:
        """Returns all bridges' device infos"""
        response = await self._session.get(
            f"{API_BASE_URL}/api/v1.25/my/bridge",
            headers={**HEADERS, "Authorization": f"PersonalKey {self._access_token}"},
        )
        json = await response.json()
        result = MyBridgeResponse.from_dict(json)
        return result.result
        pass

    async def async_get_keypads(self) -> List[Keypad]:
        """Returns all bridges' device infos"""
        response = await self._session.get(
            f"{API_BASE_URL}/api/v1.25/my/keypad",
            headers={**HEADERS, "Authorization": f"PersonalKey {self._access_token}"},
        )
        json = await response.json()
        result = MyKeypadResponse.from_dict(json)
        return result.result
        pass

    async def async_operation_lock(self, lock_id: int) -> OperationResponse:
        """Locks given lock"""
        response = await self._session.post(
            f"{API_BASE_URL}/api/v1.25/my/lock/{lock_id}/operation/lock",
            headers={
                **HEADERS,
                "Authorization": f"PersonalKey {self._access_token}",
            },
        )
        json = await response.json()
        return OperationResponse.from_dict(json)

    async def async_operation_unlock(self, lock_id: int) -> OperationResponse:
        """Unlocks given lock"""
        response = await self._session.post(
            f"{API_BASE_URL}/api/v1.25/my/lock/{lock_id}/operation/unlock",
            headers={
                **HEADERS,
                "Authorization": f"PersonalKey {self._access_token}",
            },
        )
        json = await response.json()
        return OperationResponse.from_dict(json)
