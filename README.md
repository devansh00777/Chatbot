# LangChain Chatbot with Groq

A fast and interactive AI chatbot built using Streamlit, LangChain, and Groq API with real-time streaming responses.

---

## Overview

This project demonstrates how to build a modern AI chatbot using LangChain and Groq's ultra-fast inference engine.
It includes a clean UI, streaming responses, and session-based chat history.

---

## Features

* Interactive chat interface using Streamlit
* Fast responses powered by Groq
* Real-time streaming output
* Session-based chat history
* Sidebar controls for API key and model selection

---

## Tech Stack

* Python
* Streamlit
* LangChain (Core + Groq Integration)
* Groq API

---

## Project Structure

```bash
chatbot_1/
│
├── main/
│   ├── chatbot.py
│   └── main.ipynb
│
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── README.md
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Chatbot.git
cd Chatbot
```

---

### 2. Install dependencies (using uv)

```bash
uv add -r requirements.txt
```

---

### 3. Run the application

```bash
uv run streamlit run main/chatbot.py
```

---

## Environment Variables

You can either:

* Enter your API key in the sidebar
  or
* Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## How to Use

1. Enter your Groq API key in the sidebar
2. Select a model
3. Start chatting

---

## Screenshot

(Add your app screenshot here)

---

## Future Improvements

* Conversation memory (context-aware responses)
* PDF / document chatbot
* Chat history storage
* Deployment (Streamlit Cloud / Render)
* UI improvements

---

## Author

Devansh Dangwal

---

## Support

If you like this project, consider giving it a star on GitHub.

---

## Note

This project is built for learning and demonstrating modern AI app development using LangChain and Groq.
