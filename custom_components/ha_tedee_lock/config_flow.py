"""Adds config flow for Tedee Lock."""
import logging
from typing import List, Optional

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession

from . import access_token_schema, TedeeLockApiClient
from .const import DOMAIN, CONF_PERSONAL_ACCESS_TOKEN, CONF_DEVICE_INFO, CONF_DEVICE_TYPE, CONF_DEVICE_ID
from .model.devices.device import Device
from .options_flow import TedeeLockOptionsFlow

_LOGGER = logging.getLogger(__name__)


class TedeeLockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for ha_tedee_lock."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}
        self._devices: List[Device] = []
        self._access_token: Optional[str] = None

    async def async_step_user(self, user_input: dict = None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            self._access_token = user_input.get(CONF_PERSONAL_ACCESS_TOKEN)
            try:
                self._devices = await self._get_devices()
                if self._devices:
                    return await self.async_step_select_device()
                else:
                    self._errors = {"base": "no_devices_found"}
                    return self.async_show_form(
                        step_id="user",
                        data_schema=access_token_schema(),
                        errors=self._errors,
                    )
            except Exception as ex:
                _LOGGER.exception(ex)
                self._errors = {"base": "unknown_error"}
                return self.async_show_form(
                    step_id="user",
                    data_schema=access_token_schema(user_input),
                    errors=self._errors,
                )

        else:
            self._errors = {}
            return self.async_show_form(
                step_id="user",
                data_schema=access_token_schema(user_input),
                errors=self._errors,
            )

    async def async_step_select_device(self, user_input: dict = None):
        """Shows and handles device selection form"""

        if user_input is not None:
            device = self._find_device_by_list_name(user_input.get("selected_device"))
            if device is not None:
                return self.async_create_entry(
                    title=device.name,
                    description=str(device.device_type),
                    data={
                        CONF_PERSONAL_ACCESS_TOKEN: self._access_token,
                        CONF_DEVICE_INFO: device.to_dict(),
                        CONF_DEVICE_TYPE: device.device_type.value,
                        CONF_DEVICE_ID: device.id,
                    },
                )
        else:
            device_names = [device.list_name for device in self._devices]
            schema = vol.Schema({vol.Required("selected_device"): vol.In(device_names)})
            self._errors = {}
            return self.async_show_form(
                step_id="select_device",
                data_schema=schema,
                errors=self._errors,
            )

    def _find_device_by_list_name(self, list_name: str) -> Optional[Device]:
        return next(filter(lambda x: x.list_name == list_name, self._devices))

    async def _get_devices(self) -> List[Device]:
        session = async_create_clientsession(self.hass)
        api = TedeeLockApiClient(self._access_token, session, self.hass)
        return await api.get_devices_info()

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return TedeeLockOptionsFlow(config_entry)
