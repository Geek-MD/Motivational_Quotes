"""Constants for the Motivational Quotes integration."""

from homeassistant.const import Platform

DOMAIN = "motivational_quotes"
NAME = "Motivational Quotes"
PLATFORMS = [Platform.SENSOR]

CONF_UPDATE_TIME = "update_time"
DEFAULT_UPDATE_TIME = "08:00"

DATA_QUOTES = "quotes_en.json"
DATA_FOLDER = "motivational_quotes_data"

SENSOR_NAME = "Motivational Quote"
SENSOR_UNIQUE_ID = "motivational_quote_sensor"
