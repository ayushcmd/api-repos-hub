# 💰 Finance APIs

> Best GitHub repos for Finance, Stock Market, Crypto & Payments

---

## 🌟 Top Repos

| Repo | Description | Stars | Auth |
|---|---|---|---|
| [maybe-finance/maybe](https://github.com/maybe-finance/maybe) | Open source personal finance app | 40k+ | API Key |
| [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | Curated quant finance resources | 20k+ | None |
| [ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) | Yahoo Finance market data downloader | 13k+ | None |
| [OpenBB-finance/OpenBBTerminal](https://github.com/OpenBB-finance/OpenBBTerminal) | Open source investment research platform | 30k+ | API Key |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | Finance section — all free finance APIs | 417k+ | Varies |

---

## 💸 Free Tier Highlights

| API | Free Tier | Link |
|---|---|---|
| Alpha Vantage | 25 req/day free | [alphavantage.co](https://alphavantage.co) |
| CoinGecko | Free crypto data | [coingecko.com/api](https://coingecko.com/api) |
| Yahoo Finance (yfinance) | Free via Python library | [pypi.org/project/yfinance](https://pypi.org/project/yfinance) |
| Open Exchange Rates | 1000 req/month free | [openexchangerates.org](https://openexchangerates.org) |
| Fixer.io | 100 req/month free | [fixer.io](https://fixer.io) |

---

## 📖 Quick Usage

```javascript
// CoinGecko — Free Crypto Prices (No Auth!)
const response = await fetch(
  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
);
const data = await response.json();
console.log(data.bitcoin.usd); // Bitcoin price in USD
```

---

[⬅️ Back to Main](../README.md)