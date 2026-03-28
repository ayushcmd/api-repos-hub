<!-- Banner -->
<div align="center">

![API Repos Hub Banner](assets/banner_api.png)

# ⚡ API Repos Hub

### The only directory you need — best API repos, guides & resources for developers

[![Stars](https://img.shields.io/github/stars/ayushcmd/api-repos-hub?style=for-the-badge&color=FFD700&labelColor=1a1a1a)](https://github.com/ayushcmd/api-repos-hub/stargazers)
[![Forks](https://img.shields.io/github/forks/ayushcmd/api-repos-hub?style=for-the-badge&color=FFD700&labelColor=1a1a1a)](https://github.com/ayushcmd/api-repos-hub/forks)
[![Contributors](https://img.shields.io/github/contributors/ayushcmd/api-repos-hub?style=for-the-badge&color=FFD700&labelColor=1a1a1a)](https://github.com/ayushcmd/api-repos-hub/graphs/contributors)
[![Last Updated](https://img.shields.io/github/last-commit/ayushcmd/api-repos-hub?style=for-the-badge&color=FFD700&labelColor=1a1a1a)](https://github.com/ayushcmd/api-repos-hub/commits/main)
![Repo Size](https://img.shields.io/github/repo-size/ayushcmd/api-repos-hub?color=FFD700&labelColor=1a1a1a&style=for-the-badge)
![Total APIs](https://img.shields.io/badge/Total%20APIs-50%2B-FFD700?style=for-the-badge&labelColor=1a1a1a)
![Categories](https://img.shields.io/badge/Categories-7-FFD700?style=for-the-badge&labelColor=1a1a1a)

---

> 💛 **If this repo helps you — please ⭐ Star it to save for your future projects!**
> Every star helps more developers discover this resource.

---

</div>

##  What is API Repos Hub?

A **curated directory** of the best API-related GitHub repositories across every field — so you never have to search again. Plus a clear guide on how to actually use API keys in your projects.

**Who is this for?**
-  Developers starting a new project and looking for APIs
-  Students learning how APIs work
-  Builders who want to ship faster

---

##  Categories

| # | Category | Description |
|---|---|---|
| 01 | [ AI & LLM APIs](apis/ai-llm.md) | ChatGPT, GROQ, Gemini, Together AI and more |
| 02 | [ Finance APIs](apis/finance.md) | Stock market, crypto, banking, payments |
| 03 | [ Weather APIs](apis/weather.md) | Forecasts, climate data, real-time weather |
| 04 | [ Maps & Location APIs](apis/maps-location.md) | Google Maps, OpenStreetMap, geolocation |
| 05 | [ Auth APIs](apis/auth.md) | OAuth, Google Login, GitHub Login |
| 06 | [ Communication APIs](apis/communication.md) | SMS, Email, Push notifications |
| 07 | [ Data & Analytics APIs](apis/data-analytics.md) | Datasets, analytics, visualization |

---

## 🔑 How to Use API Keys in Your Project

> Full guide → [guides/how-to-use-api-keys.md](guides/how-to-use-api-keys.md)

**Quick 4-step flow:**

```
1. Sign up on the API platform
2. Generate your API Key from dashboard
3. Save it in your .env file — NEVER hardcode it
4. Call the API using fetch/axios with your key in headers
```

**Example — GROQ AI API:**

```javascript
// .env
GROQ_API_KEY=your_key_here

// your code
const response = await fetch("https://api.groq.com/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.GROQ_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "llama-3.3-70b-versatile",
    messages: [{ role: "user", content: "Hello!" }]
  })
});
const data = await response.json();
```

⚠️ **Always add `.env` to your `.gitignore` — never push API keys to GitHub!**

---

## 💡 New to APIs? Start Here

> **Beginner?** Follow this path 👇

| Level | Type | Best For | Example |
|---|---|---|---|
| 🟢 **Zero Setup** | No Auth | First time trying APIs | [Open-Meteo](https://open-meteo.com) • [REST Countries](https://restcountries.com) • [Public APIs](https://github.com/public-apis/public-apis) |
| 🟡 **Easy Start** | API Key | Most real projects | [GROQ](https://console.groq.com) • [NASA](https://api.nasa.gov) • [OpenWeather](https://openweathermap.org/api) |
| 🔵 **Intermediate** | Bearer Token | Production apps | [GitHub API](https://docs.github.com/en/rest) • [Stripe](https://stripe.com/docs/api) |
| 🔴 **Advanced** | OAuth 2.0 | Login with Google/GitHub | [NextAuth](https://github.com/nextauthjs/next-auth) • [Supabase](https://supabase.com) |

**💰 Free tier tip:** Almost every API above has a generous free tier — no credit card needed to start!

---

## 🤝 Contributing


Want to add a repo or fix a broken link?

See → [CONTRIBUTING.md](CONTRIBUTING.md)

We welcome all contributions — big or small! 💛

<a href="https://github.com/ayushcmd/api-repos-hub/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ayushcmd/api-repos-hub"/>
</a>

---

##  License

[CC0 1.0 Universal](LICENSE) — free to use, share, and modify.

---

<div align="center">

**Made with 💛 for developers everywhere**

⭐ **Star this repo** — so you always have it when starting your next project!

</div>
