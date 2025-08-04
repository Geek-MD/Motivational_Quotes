# Motivational Quotes

**Motivational Quotes** is a custom integration for [Home Assistant](https://www.home-assistant.io/) that provides a daily dose of inspiration. It fetches motivational quotes from [BrainyQuote](https://www.brainyquote.com/topics/motivational-quotes), stores them locally, and exposes a sensor with a random quote that updates once per day at a user-defined time.

---

## 🔧 Features

- ✅ Random motivational quote updated daily  
- ✅ Author shown as an attribute  
- ✅ Local quote storage to avoid repetition  
- ✅ Configurable update time via the UI  
- ✅ Option flow support to change time later  
- ✅ Custom Lovelace card to display the quote beautifully  
- 🧪 Future support for multi-language quotes (EN/ES)  

---

## 📦 Installation

### HACS (Recommended)

1. In HACS, go to **Integrations** > **Custom Repositories**  
2. Add this repository: `https://github.com/Geek-MD/motivational-quotes`  
3. Choose **Integration** as the category  
4. Search for **Motivational Quotes** and install it  
5. Restart Home Assistant  

### Manual

1. Download this repository as a ZIP  
2. Extract it to `custom_components/motivational_quotes/` in your Home Assistant config folder  
3. Place the file `motivational-quote-card.js` in `/config/www/`  
4. Restart Home Assistant  

---

## ⚙️ Configuration

After installation:

1. Go to **Settings** → **Devices & Services** → **Add Integration**  
2. Search for `Motivational Quotes`  
3. Select your preferred time for the daily update  

You can modify the update time later by clicking **Configure** on the integration.

---

## 📊 Sensor

The integration creates a sensor:

- `sensor.motivational_quote`

**State:**

- A motivational quote  

**Attributes:**

- `author`: The person who said the quote  
- `updated_at`: Timestamp of the last update  

---

## 💡 Lovelace Card

A custom card is included to visually display the quote and author.

### Setup

1. Ensure `motivational-quote-card.js` is placed in `/config/www/`
2. Add the following to your **Resources** section:

       url: /local/motivational-quote-card.js
       type: module

   *(Or add it from Settings → Dashboards → Resources → Add Resource)*

3. Add the card to your dashboard:

       type: custom:motivational-quote-card
       entity: sensor.motivational_quote

---

## 🛠 Roadmap

- [x] English quote support  
- [x] Daily update with random selection  
- [x] Custom Lovelace card  
- [ ] Automatic scraping of new quotes  
- [ ] Translation to Spanish  
- [ ] Language selection in UI  

---

## 🐞 Issues / Feedback

Please report issues or suggest features via [GitHub Issues](https://github.com/Geek-MD/motivational-quotes/issues).

---

## 📄 License

MIT © Geek-MD
