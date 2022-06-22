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
CONF_IP_ADDRESS = "ip_address"
CONF_PORT = "port"
STATE = "state"
DATA = "data"
API_CLIENT = "api_client"

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
