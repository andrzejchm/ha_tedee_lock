"""Sample API Client."""
import logging
from typing import List
import aiohttp

from homeassistant.core import HomeAssistant

from custom_components.ha_tedee_lock.const import API_BASE_URL
from custom_components.ha_tedee_lock.model.tedee_device import TedeeDevice, TedeeBridge
from custom_components.ha_tedee_lock.model.tedee_lock import (
    TedeeLock,
    TedeeMyLocksResponse,
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

    async def get_devices(self) -> List[TedeeDevice]:
        locks = await self.get_locks()
        return [
            *locks,
            # ...(await self.get_bridges()), # TODO
        ]

    async def get_locks(self) -> List[TedeeLock]:
        response = await self._session.get(
            f"{API_BASE_URL}/api/v1.25/my/lock",
            headers={"Authorization": f"PersonalKey {self._access_token}"},
        )
        json = await response.json()
        result = TedeeMyLocksResponse.from_dict(json)
        return result.result

    async def get_bridges(self) -> List[TedeeBridge]:
        # TODO
        # result = TedeeMyBridgesResponse.from_dict(await self._session.get(f"{API_BASE_URL}/api/v1.25/my/bridge"))
        # print(result)
        # return result
        pass
