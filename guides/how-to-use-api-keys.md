# 🔑 How to Use API Keys in Your Project

> A beginner-friendly, step-by-step guide

---

## What is an API Key?

An API key is a **secret token** that identifies you when calling an API.

Think of it like:
> 🏠 API URL = Restaurant address — share freely
> 💳 API Key = Your credit card — keep private always

---

## Step 1 — Sign Up & Get Your Key

1. Go to the API platform (e.g. [console.groq.com](https://console.groq.com))
2. Create a free account
3. Go to **API Keys** section in dashboard
4. Click **"Create New Key"**
5. Copy the key — you'll only see it once!

---

## Step 2 — Save in `.env` File

Create a `.env` file in your project root:

```bash
# .env
GROQ_API_KEY=gsk_your_key_here
GEMINI_API_KEY=AIza_your_key_here
WEATHER_API_KEY=abc123_your_key_here
```

---

## Step 3 — Add `.env` to `.gitignore`

```bash
# .gitignore
.env
.env.local
.env.production
```

⚠️ **This is the most important step — never skip it!**

---

## Step 4 — Use in Your Code

### JavaScript / Node.js

```javascript
// Install dotenv first: npm install dotenv
require("dotenv").config(); // at top of file

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
console.log(data.choices[0].message.content);
```

### Python

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # loads .env file

headers = {
    "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.groq.com/v1/chat/completions",
    headers=headers,
    json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "Hello!"}]}
)
print(response.json())
```

---

## Step 5 — Set Keys in Production

On **Vercel:**
> Settings → Environment Variables → Add your key

On **Render:**
> Dashboard → Environment → Add your key

On **Railway:**
> Variables tab → Add your key

---

## Common Auth Types

| Type | How it works | Example |
|---|---|---|
| **No Auth** | Direct call — no key needed | Open-Meteo, REST Countries |
| **API Key (Header)** | Send key in `Authorization` header | GROQ, OpenAI |
| **API Key (Query)** | Send key in URL `?api_key=xxx` | NASA, Alpha Vantage |
| **OAuth 2.0** | Login flow to get token | Google, GitHub |
| **Bearer Token** | Like API key but temporary | Most modern APIs |

---

## ⚠️ Security Checklist

- [ ] `.env` in `.gitignore` ✅
- [ ] Never hardcode keys in code ✅
- [ ] Never commit `.env` to GitHub ✅
- [ ] Regenerate key if accidentally exposed ✅
- [ ] Use environment variables in production ✅

---

[⬅️ Back to Main](../README.md)