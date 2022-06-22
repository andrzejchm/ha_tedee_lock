"""Tests for Tedee Lock api."""

from _pytest.logging import LogCaptureFixture
from pytest_homeassistant_custom_component.test_util.aiohttp import AiohttpClientMocker


async def test_api(hass, aioclient_mock: AiohttpClientMocker, caplog: LogCaptureFixture):
    pass
