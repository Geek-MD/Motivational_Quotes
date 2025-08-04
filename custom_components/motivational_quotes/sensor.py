"""Sensor platform for Motivational Quotes."""
from __future__ import annotations

import logging
import os
import json
import random
from datetime import datetime

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import Entity

from .const import (
    DOMAIN,
    SENSOR_NAME,
    SENSOR_UNIQUE_ID,
    DATA_QUOTES,
    DATA_FOLDER,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    quotes_path = hass.config.path(f"custom_components/{DOMAIN}/{DATA_QUOTES}")
    sensor = MotivationalQuoteSensor(quotes_path)
    async_add_entities([sensor], update_before_add=True)

    # Guardar la referencia del sensor por si se quiere actualizar externamente
    hass.data[DOMAIN]["coordinator"] = sensor


class MotivationalQuoteSensor(SensorEntity):
    """Representation of a Motivational Quote sensor."""

    _attr_should_poll = False

    def __init__(self, quotes_file: str) -> None:
        """Initialize the sensor."""
        self._attr_name = SENSOR_NAME
        self._attr_unique_id = SENSOR_UNIQUE_ID
        self._quotes_file = quotes_file
        self._quote: str = ""
        self._author: str = ""
        self._updated_at: str = ""

    def _load_quotes(self) -> list[dict[str, str]]:
        """Load quotes from JSON file."""
        if not os.path.isfile(self._quotes_file):
            _LOGGER.warning("Quotes file not found: %s", self._quotes_file)
            return []

        try:
            with open(self._quotes_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            _LOGGER.error("Failed to read quotes file: %s", e)
            return []

    def _select_random_quote(self) -> None:
        """Select a random quote from the list."""
        quotes = self._load_quotes()
        if not quotes:
            self._quote = "Stay positive, work hard, make it happen."
            self._author = "Unknown"
            return

        selected = random.choice(quotes)
        self._quote = selected.get("quote", "No quote found")
        self._author = selected.get("author", "Unknown")
        self._updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    async def async_update(self) -> None:
        """Update the sensor with a new quote."""
        self._select_random_quote()
        self._attr_native_value = self._quote
        self._attr_extra_state_attributes = {
            "author": self._author,
            "updated_at": self._updated_at,
        }
