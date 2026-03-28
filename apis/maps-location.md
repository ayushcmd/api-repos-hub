# 🗺️ Maps & Location APIs

> Best GitHub repos for Maps, Geolocation & Location data

---

## 🌟 Top Repos

| Repo | Description | Stars | Auth |
|---|---|---|---|
| [Leaflet/Leaflet](https://github.com/Leaflet/Leaflet) | Most popular open source map library | 40k+ | None |
| [mapbox/mapbox-gl-js](https://github.com/mapbox/mapbox-gl-js) | Interactive maps with WebGL | 11k+ | API Key |
| [googlemaps/js-api-loader](https://github.com/googlemaps/js-api-loader) | Google Maps JS loader | 500+ | API Key |
| [nominatim/nominatim](https://github.com/osm-search/Nominatim) | OpenStreetMap geocoding — free | 3k+ | None |

---

## 💸 Free Tier Highlights

| API | Free Tier | Link |
|---|---|---|
| OpenStreetMap / Nominatim | Completely free | [nominatim.openstreetmap.org](https://nominatim.openstreetmap.org) |
| Mapbox | 50k map loads/month free | [mapbox.com](https://mapbox.com) |
| Google Maps | $200 free credit/month | [developers.google.com/maps](https://developers.google.com/maps) |
| ipapi | 1000 req/day free (IP geolocation) | [ipapi.co](https://ipapi.co) |

---

## 📖 Quick Usage

```javascript
// Nominatim — Free geocoding (no key needed!)
const response = await fetch(
  "https://nominatim.openstreetmap.org/search?q=Bilaspur,India&format=json"
);
const data = await response.json();
console.log(data[0].lat, data[0].lon);
```

---

[⬅️ Back to Main](../README.md)