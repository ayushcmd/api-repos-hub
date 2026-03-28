# 🤖 AI & LLM APIs

> Best GitHub repos for AI and Large Language Model APIs

---

## 🌟 Top Repos

| Repo | Description | Stars | Auth |
|---|---|---|---|
| [openai/openai-node](https://github.com/openai/openai-node) | Official OpenAI Node.js SDK | 8k+ | API Key |
| [groq/groq-typescript](https://github.com/groq/groq-typescript) | Official GROQ SDK — fastest free LLM API | 1k+ | API Key |
| [google/generative-ai-js](https://github.com/google/generative-ai-js) | Google Gemini official JS SDK | 2k+ | API Key |
| [togethercomputer/together-typescript](https://github.com/togethercomputer/together-typescript) | Together AI SDK — many free models | 500+ | API Key |
| [ollama/ollama](https://github.com/ollama/ollama) | Run LLMs locally — no API key needed | 80k+ | None |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Most popular ML model library | 130k+ | API Key |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Build LLM-powered apps | 90k+ | API Key |

---

## 💸 Free Tier Highlights

| API | Free Tier | Link |
|---|---|---|
| GROQ | 30 req/min, multiple models free | [console.groq.com](https://console.groq.com) |
| Google Gemini | 15 req/min free | [aistudio.google.com](https://aistudio.google.com) |
| Together AI | $1 free credit | [api.together.xyz](https://api.together.xyz) |
| Hugging Face | Free inference API | [huggingface.co](https://huggingface.co) |
| Ollama | Completely free — runs locally | [ollama.com](https://ollama.com) |

---

## 📖 Quick Usage

```javascript
// GROQ — Fastest free LLM
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
```

---

[⬅️ Back to Main](../README.md)