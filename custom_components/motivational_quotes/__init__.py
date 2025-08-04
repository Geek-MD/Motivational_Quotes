"""The Motivational Quotes integration."""

import asyncio
import logging
from datetime import time

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_time_change
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, PLATFORMS, CONF_UPDATE_TIME

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Motivational Quotes integration (YAML-based, unused)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Motivational Quotes from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Carga plataformas (sensor)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Obtener hora configurada
    update_time_str = entry.data.get(CONF_UPDATE_TIME, "08:00")
    hour, minute = map(int, update_time_str.split(":"))

    async def update_quotes(_now):
        """Trigger an update for the sensor platform."""
        _LOGGER.debug("Scheduled update of motivational quote at %02d:%02d", hour, minute)
        coordinator = hass.data[DOMAIN].get("coordinator")
        if coordinator:
            await coordinator.async_update_data()

    # Programar la actualización diaria
    async_track_time_change(
        hass, update_quotes, hour=hour, minute=minute, second=0
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)

    return unload_ok
