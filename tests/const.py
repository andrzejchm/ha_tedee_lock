"""Constants for Tedee Lock tests."""
from custom_components.ha_tedee_lock import CONF_DEVICE_TYPE
from custom_components.ha_tedee_lock import CONF_PERSONAL_ACCESS_TOKEN
from custom_components.ha_tedee_lock import DeviceType
from custom_components.ha_tedee_lock.const import CONF_DEVICE_ID
from custom_components.ha_tedee_lock.const import CONF_DEVICE_INFO
from custom_components.ha_tedee_lock.model.states.device_state_lock import DeviceStateLock

MOCK_DEVICE_INFO = {
    "userSettings": {
        "autoUnlockEnabled": True,
        "autoUnlockConfirmEnabled": False,
        "autoUnlockRangeIn": 100,
        "autoUnlockRangeOut": 200,
        "autoUnlockTimeout": 20,
        "autoUnlockCheckWiFi": True,
        "wiFiName": None,
        "location": {
            "latitude": 21.0134591822131117,
            "longitude": 38.997140404374477
        },
        "bellAlertDisabled": None
    },
    "connectedToId": 12830,
    "connectedToKeypadId": 11344,
    "deviceSettings": {
        "autoLockEnabled": False,
        "autoLockDelay": 15,
        "autoLockImplicitEnabled": False,
        "autoLockImplicitDelay": 5,
        "pullSpringEnabled": False,
        "pullSpringDuration": 2,
        "autoPullSpringEnabled": True,
        "postponedLockEnabled": True,
        "postponedLockDelay": 5,
        "buttonLockEnabled": True,
        "buttonUnlockEnabled": True,
        "hasUnpairedKeypad": False
    },
    "lockProperties": {
        "state": 6,
        "isCharging": False,
        "batteryLevel": 39,
        "stateChangeResult": None,
        "lastStateChangedDate": "2022-06-28T17:18:38.962"
    },
    "beaconMajor": 33221,
    "beaconMinor": 4582,
    "id": 12248,
    "organizationId": None,
    "serialNumber": "22121392-004852",
    "macAddress": "00:00:00:00:00:00",
    "name": "main door",
    "userIdentity": "0b96bdc3-3f0d-4c67-b40a-a63f1c2d9a5e",
    "type": 2,
    "created": "2022-03-23T15:35:26.0400127",
    "revision": 18,
    "deviceRevision": 13,
    "targetDeviceRevision": 13,
    "timeZone": "Europe/Amsterdam",
    "isConnected": True,
    "accessLevel": 2,
    "shareDetails": None,
    "softwareVersions": [
        {
            "softwareType": 0,
            "version": "1.4.60536",
            "updateAvailable": False
        }
    ]
}

LOCK_STATE_DICT = {
    "id": MOCK_DEVICE_INFO["id"],
    "isConnected": True,
    "lockProperties": {
        "state": 6,
        "isCharging": False,
        "batteryLevel": 45,
        "stateChangeResult": None,
        "lastStateChangedDate": "2022-06-23T15:56:31.44"
    }
}

MOCK_CONFIG = {
    CONF_PERSONAL_ACCESS_TOKEN: "sampleAccessTokenGoesHere",
    CONF_DEVICE_TYPE: DeviceType.LOCK.value,
    CONF_DEVICE_ID: LOCK_STATE_DICT["id"],
    CONF_DEVICE_INFO: MOCK_DEVICE_INFO,
}

MOCK_STATES = [
    DeviceStateLock.from_dict(LOCK_STATE_DICT),
]
