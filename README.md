# Motivational Quotes

**Motivational Quotes** is a custom integration for [Home Assistant](https://www.home-assistant.io/) that provides a daily dose of inspiration. It fetches motivational quotes from [BrainyQuote](https://www.brainyquote.com/topics/motivational-quotes), stores them locally, and exposes a sensor with a random quote that updates once per day at a user-defined time.

---

## 🔧 Features

- ✅ Random motivational quote updated daily
- ✅ Author shown as an attribute
- ✅ Local quote storage to avoid repetition
- ✅ Configurable update time via the UI
- ✅ Option flow support to change time later
- 🧪 Future support for multi-language quotes (EN/ES)

---

## 📦 Installation

### HACS (Recommended)

1. In HACS, go to **Integrations** > **Custom Repositories**.
2. Add this repository: `https://github.com/Geek-MD/motivational-quotes`
3. Choose **Integration** as the category.
4. Search for **Motivational Quotes** and install it.
5. Restart Home Assistant.

### Manual

1. Download this repository as a ZIP.
2. Extract it to `custom_components/motivational_quotes/` in your Home Assistant config folder.
3. Restart Home Assistant.

---

## ⚙️ Configuration

After installation:

1. Go to **Settings** > **Devices & Services** > **Add Integration**.
2. Search for `Motivational Quotes`.
3. Select your preferred time for the daily update.

You can modify the update time later by clicking **Configure** on the integration.

---

## 🧠 Sensor

The integration creates a sensor:

- `sensor.motivational_quote`

### State

A motivational quote.

### Attributes

- `author`: The person who said the quote
- `updated_at`: Timestamp of the last update

---

## 🛠 Roadmap

- [x] Initial English quote support
- [ ] Scraper to update quotes daily from BrainyQuote
- [ ] Automatic translation to Spanish (`quotes_es.json`)
- [ ] Language selection via UI

---

## 🐞 Issues / Feedback

Please report issues or suggest features via [GitHub Issues](https://github.com/Geek-MD/motivational-quotes/issues).

---

## 📄 License

MIT © Geek-MD
