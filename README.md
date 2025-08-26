
<h1 align="center">
  🔍 Input Type API
</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=24&duration=4000&pause=1000&color=3AA6FF&center=true&vCenter=true&random=false&width=600&lines=Detect+any+input+type+%F0%9F%94%8D;String+%7C+Number+%7C+Hash+%7C+Email+%7C+More!;Fast+%7C+Simple+%7C+Scalable+API+%E2%9A%A1" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Flask-API-blue?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Frontend-HTML%2FJS-orange?style=for-the-badge&logo=javascript&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## ⚡ About the Project
The **Input Type API** is a simple but powerful project where you can check what kind of input is provided:
- 🔤 String
- 🔢 Number
- 🔑 Hash (MD5, SHA1, SHA256…)
- 📧 Email
- 🌍 URL
- ☎️ Phone Numbers
- And much more!

## The app also keeps a history of the **last 5 inputs** checked.

This can be used in **validation systems**, **data cleaning tools**, or even as a **mini microservice** for developers.

---

## 📂 Project Structure

```bash
input-type-api/
│── app.py              # Flask backend
│── static/
│   └── script.js       # frontend logic
│── templates/
│   └── index.html      # frontend UI
````

---

## 🚀 How to Run Locally

```bash
# 1️⃣ Clone this repo
git clone https://github.com/your-username/input-type-api.git
cd input-type-api

# 2️⃣ Install dependencies
pip install flask

# 3️⃣ Run the backend
python app.py

# 4️⃣ Open in browser
http://127.0.0.1:5000
```

---

## 🎯 Features

✅ Detects multiple input types
✅ API + Frontend integration
✅ Real-time validation with **JS fetch()**
✅ Clean UI with Tailwind CSS
✅ Extensible → Add more input types easily
✅ Stores the last **5 checked inputs** in session history.

---

## 🖼️ Demo UI Preview

<p align="center">
  <img src="https://github.com/ShAiDSk/input-type-api/blob/main/DEMO1.png" width="600" alt="Demo Preview"/>
</p>

<p align="center">
  <img src="https://github.com/ShAiDSk/input-type-api/blob/main/DEMO2.png" width="600" alt="Demo Preview"/>
</p>

---

## 📡 API Usage

### Endpoint

```
POST /detect
```

### Request

```json
{
  "input": "hello123"
}
```

### Response

```json
{
  "input": "hello123",
  "type": "string"
}
```

---

## ⚙️ Tech Stack

* 🐍 **Flask** (Python Backend)
* 🎨 **HTML, CSS, JavaScript** (Frontend)
* 🚀 **REST API**

---

<details>
  <summary>📌 Future Improvements</summary>

* 🔮 Add AI-powered detection
* 📱 Deploy with Docker
* ☁️ Host on Render / Vercel
* 🔒 Add rate limiting + auth

</details>

---

## 🤝 Contributing

Contributions are always welcome! 🎉
Just **fork**, **create a branch**, and **submit a PR**.

---

## 📜 License

MIT License © 2025 \ShAiDSk

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=4000&pause=1000&color=FF5733&center=true&vCenter=true&random=false&width=600&lines=Made+with+❤️+by+itz.shaidsk;Keep+Building+Keep+Learning!+🚀" alt="Typing Animation" />
</p>

---



