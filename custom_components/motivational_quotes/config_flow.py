"""Config flow for Motivational Quotes integration."""
from __future__ import annotations

import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_NAME
from homeassistant.helpers.selector import selector
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, CONF_UPDATE_TIME, DEFAULT_UPDATE_TIME

_LOGGER = logging.getLogger(__name__)


class MotivationalQuotesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Motivational Quotes."""

    VERSION = 1

    async def async_step_user(self, user_input: ConfigType | None = None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Motivational Quotes", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_UPDATE_TIME, default=DEFAULT_UPDATE_TIME): selector({
                    "time": {}
                })
            })
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return MotivationalQuotesOptionsFlow(config_entry)


class MotivationalQuotesOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(self, user_input: ConfigType | None = None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_UPDATE_TIME,
                    default=self.config_entry.options.get(CONF_UPDATE_TIME, self.config_entry.data.get(CONF_UPDATE_TIME, DEFAULT_UPDATE_TIME))
                ): selector({"time": {}})
            })
        )
