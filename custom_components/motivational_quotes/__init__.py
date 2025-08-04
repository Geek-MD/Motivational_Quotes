"""The Motivational Quotes integration."""

import logging
from datetime import time

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_change
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, PLATFORMS, CONF_UPDATE_TIME

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Motivational Quotes integration (YAML not supported)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Motivational Quotes from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Forward sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Get update time (default to "08:00")
    update_time_str = entry.data.get(CONF_UPDATE_TIME, "08:00")
    time_parts = update_time_str.split(":")
    try:
        hour = int(time_parts[0])
        minute = int(time_parts[1])
    except (ValueError, IndexError):
        _LOGGER.warning("Invalid time format '%s', defaulting to 08:00", update_time_str)
        hour, minute = 8, 0

    async def update_quotes(_now):
        """Trigger an update for the sensor platform."""
        _LOGGER.debug("Scheduled update of motivational quote at %02d:%02d", hour, minute)
        coordinator = hass.data[DOMAIN].get("coordinator")
        if coordinator:
            await coordinator.async_update()

    # Schedule daily update
    async_track_time_change(
        hass,
        update_quotes,
        hour=hour,
        minute=minute,
        second=0,
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)

    return unload_ok
