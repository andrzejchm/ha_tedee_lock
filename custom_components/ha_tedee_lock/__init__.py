"""
Custom integration to integrate Tedee Lock with Home Assistant.

For more details about this integration, please refer to
https://github.com/andrzejchm/ha_tedee_lock
"""
import asyncio
import logging
from typing import Dict
from typing import Optional

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .api import TedeeLockApiClient
from .const import API_CLIENT, CONF_PERSONAL_ACCESS_TOKEN
from .const import DATA
from .const import DEFAULT_PORT
from .const import DOMAIN
from .const import PLATFORMS
from .const import STARTUP_MESSAGE

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        _LOGGER.info(STARTUP_MESSAGE)
    return False


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    unloaded = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unloaded


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)


def access_token_schema(
        user_input: Optional[Dict[str, any]] = None,
) -> vol.Schema:
    """creates schema for config flow and options flow"""
    return vol.Schema({
        vol.Required(
            CONF_PERSONAL_ACCESS_TOKEN,
            default=(user_input or {}).get(CONF_PERSONAL_ACCESS_TOKEN),
        ): str
    })
