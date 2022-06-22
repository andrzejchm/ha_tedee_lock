"""Test Tedee Lock setup process."""
from unittest.mock import patch

import pytest
from custom_components.ha_tedee_lock import async_reload_entry
from custom_components.ha_tedee_lock import async_setup_entry
from custom_components.ha_tedee_lock import async_unload_entry
from custom_components.ha_tedee_lock import TedeeUpdateCoordinator
from custom_components.ha_tedee_lock.const import DOMAIN
from homeassistant.exceptions import ConfigEntryNotReady
from pytest_homeassistant_custom_component.common import MockConfigEntry

from .const import MOCK_CONFIG
from .const import MOCK_STATES


# We can pass fixtures as defined in conftest.py to tell pytest to use the fixture
# for a given test. We can also leverage fixtures and mocks that are available in
# Home Assistant using the pytest_homeassistant_custom_component plugin.
# Assertions allow you to verify that the return value of whatever is on the left
# side of the assertion matches with the right side.
async def test_setup_unload_and_reload_entry(hass):
    """Test entry setup and unload."""
    with patch(
            "custom_components.ha_tedee_lock.TedeeLockApiClient.async_get_devices_states",
            return_value=MOCK_STATES,
    ):
        # Create a mock entry so we don't have to go through config flow
        config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")

        # Set up the entry and assert that the values set during setup are where we expect
        # them to be.
        assert await async_setup_entry(hass, config_entry)
        assert DOMAIN in hass.data and config_entry.entry_id in hass.data[DOMAIN]
        assert (isinstance(hass.data[DOMAIN][config_entry.entry_id], TedeeUpdateCoordinator))

        # Reload the entry and assert that the data from above is still there
        assert await async_reload_entry(hass, config_entry) is None
        assert DOMAIN in hass.data and config_entry.entry_id in hass.data[DOMAIN]
        assert (isinstance(hass.data[DOMAIN][config_entry.entry_id], TedeeUpdateCoordinator))

        # Unload the entry and verify that the data has been removed
        assert await async_unload_entry(hass, config_entry)
        assert config_entry.entry_id not in hass.data[DOMAIN]


async def test_setup_entry_exception(hass, error_on_get_data):
    """Test ConfigEntryNotReady when API raises an exception during entry setup."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")

    # In this case we are testing the condition where async_setup_entry raises
    # ConfigEntryNotReady using the `error_on_get_data` fixture which simulates
    # an error.
    with pytest.raises(ConfigEntryNotReady):
        assert await async_setup_entry(hass, config_entry)
