"""Sensor platform for Motivational Quotes."""
from __future__ import annotations

import logging
import os
import json
import random
from datetime import datetime

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import Entity

from .const import (
    DOMAIN,
    SENSOR_NAME,
    SENSOR_UNIQUE_ID,
    DATA_QUOTES,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    quotes_path = hass.config.path(f"custom_components/{DOMAIN}/{DATA_QUOTES}")
    sensor = MotivationalQuoteSensor(hass, quotes_path)
    async_add_entities([sensor], update_before_add=True)

    # Store the reference to allow external triggering (from __init__.py)
    hass.data[DOMAIN]["coordinator"] = sensor


class MotivationalQuoteSensor(SensorEntity):
    """Representation of a Motivational Quote sensor."""

    _attr_should_poll = False

    def __init__(self, hass: HomeAssistant, quotes_file: str) -> None:
        """Initialize the sensor."""
        self.hass = hass
        self._quotes_file = quotes_file
        self._attr_name = SENSOR_NAME
        self._attr_unique_id = SENSOR_UNIQUE_ID
        self._attr_native_value = None
        self._attr_extra_state_attributes = {}

    def _read_quotes_file(self) -> list[dict[str, str]]:
        """Blocking: read quotes from JSON file."""
        if not os.path.isfile(self._quotes_file):
            _LOGGER.warning("Quotes file not found: %s", self._quotes_file)
            return []

        try:
            with open(self._quotes_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            _LOGGER.error("Failed to read quotes file: %s", e)
            return []

    async def _load_quotes(self) -> list[dict[str, str]]:
        """Non-blocking async wrapper for file reading."""
        return await self.hass.async_add_executor_job(self._read_quotes_file)

    async def _select_random_quote(self) -> None:
        """Pick a random quote from the file."""
        quotes = await self._load_quotes()
        if not quotes:
            self._attr_native_value = "Stay positive, work hard, make it happen."
            self._attr_extra_state_attributes = {
                "author": "Unknown",
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            return

        selected = random.choice(quotes)
        quote = selected.get("quote", "No quote found")
        author = selected.get("author", "Unknown")

        self._attr_native_value = quote
        self._attr_extra_state_attributes = {
            "author": author,
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    async def async_update(self) -> None:
        """Update the sensor with a new quote."""
        await self._select_random_quote()
