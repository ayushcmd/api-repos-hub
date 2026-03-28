# 🔐 Auth APIs

> Best GitHub repos for Authentication, OAuth & Identity

---

## 🌟 Top Repos

| Repo | Description | Stars | Auth |
|---|---|---|---|
| [nextauthjs/next-auth](https://github.com/nextauthjs/next-auth) | Auth for Next.js — Google, GitHub, etc | 24k+ | OAuth |
| [supabase/supabase](https://github.com/supabase/supabase) | Open source Firebase with auth | 70k+ | API Key |
| [clerkinc/clerk](https://github.com/clerk/javascript) | Drop-in auth UI components | 3k+ | API Key |
| [lucia-auth/lucia](https://github.com/lucia-auth/lucia) | Simple session-based auth library | 9k+ | None |
| [panva/node-openid-client](https://github.com/panva/node-openid-client) | OpenID Connect client | 4k+ | OAuth |

---

## 💸 Free Tier Highlights

| API | Free Tier | Link |
|---|---|---|
| Google OAuth | Free | [console.cloud.google.com](https://console.cloud.google.com) |
| GitHub OAuth | Free | [github.com/settings/developers](https://github.com/settings/developers) |
| Supabase Auth | 50k monthly active users free | [supabase.com](https://supabase.com) |
| Clerk | 10k monthly active users free | [clerk.com](https://clerk.com) |
| Auth0 | 7500 active users free | [auth0.com](https://auth0.com) |

---

## 📖 Quick Usage

```javascript
// Google OAuth callback example (Express)
app.get("/auth/google/callback", async (req, res) => {
  const { code } = req.query;
  const tokenResponse = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      code,
      client_id: process.env.GOOGLE_CLIENT_ID,
      client_secret: process.env.GOOGLE_CLIENT_SECRET,
      redirect_uri: process.env.REDIRECT_URI,
      grant_type: "authorization_code"
    })
  });
  const tokens = await tokenResponse.json();
});
```

---

[⬅️ Back to Main](../README.md)