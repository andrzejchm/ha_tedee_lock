"""Test Tedee Lock config flow."""
from unittest.mock import patch

import pytest
from custom_components.ha_tedee_lock import DeviceType
from custom_components.ha_tedee_lock.const import CONF_DEVICE_INFO
from custom_components.ha_tedee_lock.const import CONF_DEVICE_TYPE
from custom_components.ha_tedee_lock.const import CONF_PERSONAL_ACCESS_TOKEN
from custom_components.ha_tedee_lock.const import DOMAIN
from homeassistant import config_entries
from homeassistant import data_entry_flow
from pytest_homeassistant_custom_component.test_util.aiohttp import AiohttpClientMocker
from tests.const import MOCK_CONFIG
from tests.const import MOCK_DEVICE_INFO


# This fixture bypasses the actual setup of the integration
# since we only want to test the config flow. We test the
# actual functionality of the integration in other test modules.


@pytest.fixture(autouse=True)
def bypass_setup_fixture():
    """Prevent setup."""
    with patch(
            "custom_components.ha_tedee_lock.async_setup_entry",
            return_value=True,
    ):
        yield


# Here we simiulate a successful config flow from the backend.
# Note that we use the `bypass_get_data` fixture here because
# we want the config flow validation to succeed during the test.
async def test_successful_config_flow(hass, aioclient_mock: AiohttpClientMocker):
    """Test a successful config flow."""
    await _mock_device_info(aioclient_mock)

    # Initialize a config flow
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    # Check that the config flow shows the user form as the first step
    assert result["type"] == data_entry_flow.RESULT_TYPE_FORM
    assert result["step_id"] == "user"

    # If a user were to enter `test_username` for username and `test_password`
    # for password, it would result in this function call
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], user_input={CONF_PERSONAL_ACCESS_TOKEN: MOCK_CONFIG[CONF_PERSONAL_ACCESS_TOKEN]}
    )

    # Check that the config flow is complete and a new entry is created with
    # the input data
    assert result["type"] == data_entry_flow.RESULT_TYPE_FORM
    assert result["errors"] == {}
    assert result["step_id"] == "select_device"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], user_input={"selected_device": 'Lock: "main door" (SN: 22121392-004852)'}
    )
    assert result["type"] == data_entry_flow.RESULT_TYPE_CREATE_ENTRY
    assert result["title"] == "main door"
    assert result["data"][CONF_PERSONAL_ACCESS_TOKEN] == MOCK_CONFIG[CONF_PERSONAL_ACCESS_TOKEN]
    assert result["data"][CONF_DEVICE_TYPE] == DeviceType.LOCK.value
    assert result["data"][CONF_DEVICE_INFO]["id"] == MOCK_DEVICE_INFO["id"]
    assert result["result"]


# In this case, we want to simulate a failure during the config flow.
# We use the `error_on_get_data` mock instead of `bypass_get_data`
# (note the function parameters) to raise an Exception during
# validation of the input config.
async def test_failed_config_flow(hass, error_on_get_data):
    """Test a failed config flow due to credential validation failure."""

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    assert result["type"] == data_entry_flow.RESULT_TYPE_FORM
    assert result["step_id"] == "user"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], user_input={CONF_PERSONAL_ACCESS_TOKEN: MOCK_CONFIG[CONF_PERSONAL_ACCESS_TOKEN], }
    )

    assert result["type"] == data_entry_flow.RESULT_TYPE_FORM
    assert result["errors"] == {"base": "unknown_error"}


async def _mock_device_info(aioclient_mock: AiohttpClientMocker):
    aioclient_mock.get(
        "https://api.tedee.com/api/v1.25/my/lock",
        json={
            "result": [MOCK_DEVICE_INFO],
            "success": True,
            "errorMessages": [],
            "statusCode": 200
        },
    )
