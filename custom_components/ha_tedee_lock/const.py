"""Constants for Tedee Lock."""
# Base component constants
NAME = "Tedee Lock"
DOMAIN = "ha_tedee_lock"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "1.0.0"

ISSUE_URL = "https://github.com/andrzejchm/ha_tedee_lock/issues"

# Platforms
LOCK = "lock"
SENSOR = "sensor"
PLATFORMS = [LOCK, SENSOR]

# Configuration and options
CONF_PERSONAL_ACCESS_TOKEN = "personal_access_token"
CONF_DEVICE_ID = "device_id"
CONF_DEVICE_TYPE = "device_type"
STATE = "state"
DATA = "data"
API_CLIENT = "api_client"
API_BASE_URL = "https://api.tedee.com"

# Defaults
DEFAULT_NAME = DOMAIN
DEFAULT_PORT = 80

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
