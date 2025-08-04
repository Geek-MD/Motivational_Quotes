class MotivationalQuoteCard extends HTMLElement {
  setConfig(config) {
    if (!config.entity) {
      throw new Error("Entity is required.");
    }

    this._config = config;
    this.innerHTML = `
      <ha-card header="💡 Motivational Quote">
        <div class="quote-container">
          <blockquote id="quote">Loading...</blockquote>
          <div id="author" class="author"></div>
        </div>
      </ha-card>
      <style>
        .quote-container {
          padding: 16px;
          font-family: Georgia, serif;
        }
        blockquote {
          font-size: 1.2em;
          margin: 0;
          quotes: "“" "”" "‘" "’";
        }
        blockquote::before {
          content: open-quote;
        }
        blockquote::after {
          content: close-quote;
        }
        .author {
          text-align: right;
          margin-top: 8px;
          font-style: italic;
          color: #555;
        }
      </style>
    `;
  }

  set hass(hass) {
    const entityId = this._config.entity;
    const state = hass.states[entityId];

    if (!state) {
      this.innerHTML = `<ha-card><div class="card-content">Entity not found: ${entityId}</div></ha-card>`;
      return;
    }

    const quote = state.state;
    const author = state.attributes.author || "Unknown";

    this.querySelector("#quote").innerText = quote;
    this.querySelector("#author").innerText = `– ${author}`;
  }

  getCardSize() {
    return 2;
  }
}

customElements.define("motivational-quote-card", MotivationalQuoteCard);
