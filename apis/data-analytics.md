# 📊 Data & Analytics APIs

> Best GitHub repos for Datasets, Analytics & Visualization

---

## 🌟 Top Repos

| Repo | Description | Stars | Auth |
|---|---|---|---|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | Master list of all free public APIs | 417k+ | Varies |
| [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | Curated list of public datasets | 60k+ | None |
| [jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook) | Free data science handbook | 42k+ | None |
| [apache/superset](https://github.com/apache/superset) | Open source data visualization platform | 62k+ | None |
| [metabase/metabase](https://github.com/metabase/metabase) | Open source analytics & BI tool | 38k+ | None |

---

## 💸 Free Tier Highlights

| API | Free Tier | Link |
|---|---|---|
| REST Countries | Completely free | [restcountries.com](https://restcountries.com) |
| Open Disease Data | Completely free | [disease.sh](https://disease.sh) |
| World Bank API | Completely free | [api.worldbank.org](https://api.worldbank.org) |
| NASA APIs | Free with key | [api.nasa.gov](https://api.nasa.gov) |
| data.gov | Completely free | [api.data.gov](https://api.data.gov) |

---

## 📖 Quick Usage

```javascript
// REST Countries — No key needed!
const response = await fetch("https://restcountries.com/v3.1/name/india");
const data = await response.json();
console.log(data[0].population); // India's population

// NASA APOD — Astronomy Picture of the Day
const nasa = await fetch(
  `https://api.nasa.gov/planetary/apod?api_key=${process.env.NASA_API_KEY}`
);
const apod = await nasa.json();
console.log(apod.title, apod.url);
```

---

[⬅️ Back to Main](../README.md)