"""Tests for Tedee Lock api."""
import pytest
from _pytest.logging import LogCaptureFixture
from custom_components.ha_tedee_lock import DeviceType
from custom_components.ha_tedee_lock import TedeeLockApiClient
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from pytest_homeassistant_custom_component.test_util.aiohttp import AiohttpClientMocker
from tests.const import LOCK_STATE_DICT
from tests.const import MOCK_DEVICE_INFO


async def test_api(hass, aioclient_mock: AiohttpClientMocker, caplog: LogCaptureFixture):
    """Test API calls."""

    # To test the api submodule, we first create an instance of our API client
    api = TedeeLockApiClient(
        "accessToken",
        async_get_clientsession(hass),
        hass,
    )

    # Use aioclient_mock which is provided by `pytest_homeassistant_custom_components`
    # to mock responses to aiohttp requests. In this case we are telling the mock to
    # return {"test": "test"} when a `GET` call is made to the specified URL. We then
    # call `async_get_data` which will make that `GET` request.
    aioclient_mock.get(
        "https://api.tedee.com/api/v1.25/my/lock",
        json={
            "result": [MOCK_DEVICE_INFO],
            "success": True,
            "errorMessages": [],
            "statusCode": 200
        },
    )
    result = await api.async_get_devices_info()
    assert result[0].id == MOCK_DEVICE_INFO["id"]
    assert result[0].device_type == DeviceType.LOCK
    assert result[0].name == "main door"
    aioclient_mock.clear_requests()

    aioclient_mock.get("https://api.tedee.com/api/v1.25/my/lock/sync",
                       json={
                           "result": [LOCK_STATE_DICT],
                           "success": True,
                           "errorMessages": [],
                           "statusCode": 200
                       },
                       )

    result = await api.async_get_devices_states()
    assert result[0].id == MOCK_DEVICE_INFO["id"]
    assert result[0].device_type == DeviceType.LOCK

    aioclient_mock.clear_requests()

    aioclient_mock.get(
        "https://api.tedee.com/api/v1.25/my/lock/sync", exc=TimeoutError
    )
    with pytest.raises(TimeoutError):
        await api.async_get_devices_states()

    aioclient_mock.clear_requests()
    aioclient_mock.get(
        "https://api.tedee.com/api/v1.25/my/lock/sync", json={"something": "else"}
    )
    with pytest.raises(AssertionError):
        await api.async_get_locks_states()
