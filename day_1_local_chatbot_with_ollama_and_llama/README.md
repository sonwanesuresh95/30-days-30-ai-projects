# 🤖 Day 1 — Local Chatbot with Ollama + LLaMA

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Ollama](https://img.shields.io/badge/Ollama-Enabled-green)
![LLaMA](https://img.shields.io/badge/LLaMA-3.1-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

> 🚀 **A blazing-fast, local AI chatbot** powered by [Ollama](https://ollama.com) and **LLaMA** models.

---

## ✨ Features
- 💬 Chat with LLaMA 3.1 locally
- ⚡ Uses **Ollama** for optimized model loading
- 🔧 Easy to configure via `.env`
- 🐳 Docker support out-of-the-box

---

## 🚀 Quickstart

1️⃣ **Install Ollama**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2️⃣ **Pull a model** (example: `llama3:8b`)
```bash
ollama pull llama3:8b
```

3️⃣ **Edit environment variables**
```bash
nano .env
```

4️⃣ **Install dependencies**
```bash
poetry install
```

5️⃣ **Run the chatbot**
```bash
python -m src.chatbot.main
# Or with Docker
docker compose up --build
```

---

## 📸 Screenshot
![Chat Screenshot](https://via.placeholder.com/800x400?text=Chatbot+Demo)

---

## 📜 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---