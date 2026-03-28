# 🌤️ Weather APIs

> Best GitHub repos for Weather, Climate & Forecast data

---

## 🌟 Top Repos

| Repo | Description | Stars | Auth |
|---|---|---|---|
| [open-meteo/open-meteo](https://github.com/open-meteo/open-meteo) | Free weather API — no key needed! | 3k+ | None |
| [erikflowers/weather-icons](https://github.com/erikflowers/weather-icons) | 222 weather icons for UI | 12k+ | None |
| [vieraboschkova/CHAP](https://github.com/codeforboston/cliff-effects) | Climate & health data | 1k+ | None |

---

## 💸 Free Tier Highlights

| API | Free Tier | Link |
|---|---|---|
| Open-Meteo | Completely free, no key | [open-meteo.com](https://open-meteo.com) |
| OpenWeatherMap | 1000 req/day free | [openweathermap.org](https://openweathermap.org/api) |
| WeatherAPI | 1M req/month free | [weatherapi.com](https://weatherapi.com) |
| Tomorrow.io | 500 req/day free | [tomorrow.io](https://tomorrow.io) |

---

## 📖 Quick Usage

```javascript
// Open-Meteo — Completely FREE, no API key!
const response = await fetch(
  "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"
);
const data = await response.json();
console.log(data.current_weather.temperature); // Current temp
```

---

[⬅️ Back to Main](../README.md)