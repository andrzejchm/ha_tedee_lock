"""options flow"""
import logging

from homeassistant import config_entries
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_create_clientsession

from . import access_token_schema
from . import TedeeLockApiClient

_LOGGER = logging.getLogger(__name__)


class TedeeLockOptionsFlow(config_entries.OptionsFlow):
    """Config flow options handler for ha_tedee_lock."""

    def __init__(self, config_entry: ConfigEntry):
        """Initialize HACS options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)
        self._errors = {}
        self.device_info = {}

    async def async_step_init(self, user_input=None):  # pylint: disable=unused-argument
        """Manage the options."""
        return await self.async_step_user(user_input)

    async def async_step_user(self, user_input: dict = None):
        """Handle a flow initialized by the user."""
        pass

    async def _update_options(self):
        """Update config entry options."""
        return self.async_create_entry(
            title=self.device_info.get('deviceName'),
            data=self.options,
        )
