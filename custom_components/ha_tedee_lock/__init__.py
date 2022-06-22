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
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .api import TedeeLockApiClient
from .const import CONF_DEVICE_INFO
from .const import CONF_DEVICE_TYPE
from .const import CONF_PERSONAL_ACCESS_TOKEN
from .const import DOMAIN
from .const import PLATFORMS
from .const import STARTUP_MESSAGE
from .data_update_coordinator import TedeeUpdateCoordinator
from .model.device_type import DeviceType
from .model.devices.device import Device
from .model.devices.lock import Lock

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        _LOGGER.info(STARTUP_MESSAGE)

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN].setdefault(entry.entry_id, {})
    token = entry.data.get(CONF_PERSONAL_ACCESS_TOKEN)
    device_info_dict = entry.data.get(CONF_DEVICE_INFO)
    device_type = DeviceType(entry.data.get(CONF_DEVICE_TYPE))
    session = async_get_clientsession(hass)
    api_client = TedeeLockApiClient(token, session, hass)
    coordinator = TedeeUpdateCoordinator(
        hass=hass,
        api=api_client,
    )

    device = device_from_dict(device_info_dict, device_type=device_type)
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await _refresh_tedee_data(coordinator, device)

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)
    return True


async def _refresh_tedee_data(
        coordinator: DataUpdateCoordinator,
        device: Device,
):
    try:
        await coordinator.async_config_entry_first_refresh()
        if not coordinator.data.get(device.data_key):
            raise ConfigEntryNotReady(
                f"missing device info for ({device.device_type}) id: {device.id}"
            )
    except ConfigEntryNotReady as ex:
        _LOGGER.exception(ex)
        raise ex
    except Exception as ex:
        _LOGGER.exception(ex)
        message = f"could not set up Tedee device: {ex}"
        raise ConfigEntryNotReady(message)


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
    return vol.Schema(
        {
            vol.Required(
                CONF_PERSONAL_ACCESS_TOKEN,
                default=(user_input or {}).get(CONF_PERSONAL_ACCESS_TOKEN),
            ): str
        }
    )


def device_from_dict(
        device_info: dict,
        device_type: DeviceType,
) -> Device:
    if device_type == DeviceType.LOCK:
        return Lock.from_dict(device_info)
    else:
        raise f"Could not parse device_info, unknown type: {device_type}"
