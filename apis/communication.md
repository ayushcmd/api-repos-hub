# 📱 Communication APIs

> Best GitHub repos for SMS, Email & Push Notifications

---

## 🌟 Top Repos

| Repo | Description | Stars | Auth |
|---|---|---|---|
| [nodemailer/nodemailer](https://github.com/nodemailer/nodemailer) | Send emails from Node.js | 16k+ | SMTP |
| [twilio/twilio-node](https://github.com/twilio/twilio-node) | SMS & WhatsApp via Twilio | 3k+ | API Key |
| [resend/resend-node](https://github.com/resend/resend-node) | Modern email API for developers | 1k+ | API Key |
| [firebase/firebase-js-sdk](https://github.com/firebase/firebase-js-sdk) | Push notifications via FCM | 5k+ | API Key |

---

## 💸 Free Tier Highlights

| API | Free Tier | Link |
|---|---|---|
| Resend | 3000 emails/month free | [resend.com](https://resend.com) |
| Nodemailer + Gmail | Free via Gmail SMTP | [nodemailer.com](https://nodemailer.com) |
| Twilio | Free trial credits | [twilio.com](https://twilio.com) |
| Firebase FCM | Free push notifications | [firebase.google.com](https://firebase.google.com) |
| EmailJS | 200 emails/month free | [emailjs.com](https://emailjs.com) |

---

## 📖 Quick Usage

```javascript
// Resend — Modern email API
const response = await fetch("https://api.resend.com/emails", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.RESEND_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    from: "you@yourdomain.com",
    to: "user@example.com",
    subject: "Hello!",
    html: "<p>Sent via Resend API 🚀</p>"
  })
});
```

---

[⬅️ Back to Main](../README.md)