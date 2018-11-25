import binascii
import logging
import socket

import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_HOST, CONF_MAC, CONF_NAME, CONF_TIMEOUT)
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

REQUIREMENTS = ['broadlink==0.8']

_LOGGER = logging.getLogger(__name__)

DEVICE_DEFAULT_NAME = 'Broadlink SPx Power Sensor'
DEFAULT_TIMEOUT = 10

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEVICE_DEFAULT_NAME): vol.Coerce(str),
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_MAC): cv.string,
    vol.Optional(CONF_TIMEOUT, default=DEFAULT_TIMEOUT): cv.positive_int
})


# pylint: disable=unused-argument
def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([BroadlinkPowerSensor(config)])


class BroadlinkPowerSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, config):
        """Initialize the sensor."""
        import broadlink

        mac = config.get(CONF_MAC).encode().replace(b':', b'')
        mac_addr = binascii.unhexlify(mac)

        self._device = broadlink.sp2((config.get(CONF_HOST), 80), mac_addr, '0x947a')
        self._device.timeout = config.get(CONF_TIMEOUT)

        if not self._auth():
            _LOGGER.warning("Failed to connect to device")

        self._name = config.get(CONF_NAME)
        self._state = None
        self._unit_of_measurement = "W"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    def _auth(self, retry=3):
        try:
            auth = self._device.auth()
        except socket.timeout:
            auth = False
        if not auth and retry > 0:
            return self._auth(retry - 1)
        return auth

    def update(self):
        """Fetch new state data for the sensor.

           This is the only method that should fetch new data for Home Assistant.
        """
        retry = 0
        try:
            packet = bytearray([8, 0, 254, 1, 5, 1, 0, 0, 0, 45])
            response = self._device.send_packet(0x6a, packet)
            err = response[0x22] | (response[0x23] << 8)
            if err == 0:
                payload = self._device.decrypt(bytes(response[0x38:]))
                energy = int(hex(payload[7] * 256 + payload[6])[2:]) + int(hex(payload[5])[2:]) / 100.0
                self._state = energy
            else:
                self._state = 0
        except socket.timeout as error:
            if retry < 1:
                _LOGGER.error(error)
                return
        except vol.Invalid:
            self._state = 0
        if retry > 0 and self._auth():
            self._update(retry - 1)
