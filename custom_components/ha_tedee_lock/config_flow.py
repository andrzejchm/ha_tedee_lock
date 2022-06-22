"""Adds config flow for Tedee Lock."""
import logging
from typing import Dict
from typing import Optional

from homeassistant import config_entries
from homeassistant.core import callback

from . import create_schema
from .const import DOMAIN
from .options_flow import TedeeLockOptionsFlow

_LOGGER = logging.getLogger(__name__)


class TedeeLockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for ha_tedee_lock."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input: dict = None):
        """Handle a flow initialized by the user."""
        self._errors = {}

        return await self._show_config_form(user_input)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return TedeeLockOptionsFlow(config_entry)

    async def _show_config_form(
            self,
            user_input: Optional[Dict[str, any]],
    ):
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=create_schema(user_input),
            errors=self._errors,
        )
