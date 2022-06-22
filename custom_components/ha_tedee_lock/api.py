"""Sample API Client."""
import logging

import aiohttp
from homeassistant.core import HomeAssistant

TIMEOUT = 10

_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class TedeeLockApiClient:
    """Api client for Tedee Lock"""

    def __init__(
            self,
            ip_address: str,
            port: int,
            session: aiohttp.ClientSession,
            hass: HomeAssistant,
    ) -> None:
        """Sample API Client."""
        self._ip_address = ip_address
        self._port = port
        self._session = session
        self._hass = hass
