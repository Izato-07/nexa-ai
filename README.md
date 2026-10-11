# 🤖 Nexa AI

**Nexa AI** is a web-based AI assistant built with Python and Streamlit, powered by the Groq API. It provides a simple, interactive chat interface where users can ask questions and receive AI-generated responses.

## ✨ Features

- 💬 Interactive AI chat interface
- ⚡ Fast AI responses powered by Groq
- 🧠 Customizable system instructions
- 💭 Conversation context for follow-up questions
- 🗑️ Clear conversation functionality
- 🔐 API key management using Streamlit Secrets
- 🌐 Web-based interface accessible through a browser

## 🛠️ Tech Stack

- **Language:** Python
- **Frontend and UI:** Streamlit
- **AI Provider:** Groq API
- **AI Model:** OpenAI GPT-OSS 120B (`openai/gpt-oss-120b`)

## 📁 Project Structure

```text
nexa-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

**Note:** The `.streamlit/secrets.toml` file stores your local API key and must not be uploaded to GitHub.

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/Izato-07/nexa-ai.git
cd nexa-ai
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.streamlit` folder in the project directory, then create a file named `secrets.toml` inside it.

Add the following line:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Replace the placeholder with your own API key from the [Groq Console](https://console.groq.com/keys).

**Security:** Never share your API key or commit your `secrets.toml` file to a public repository.

### 4. Run the application

```bash
python -m streamlit run app.py
```

Your browser will open the Nexa AI application.

## ☁️ Deployment

Nexa AI can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/).

1. Connect your GitHub repository.
2. Select `app.py` as the application entry point.
3. Add `GROQ_API_KEY` to the app's Secrets settings.
4. Deploy the application.

## 🔒 Security

- API keys are read from Streamlit Secrets rather than hardcoded into the application.
- Never commit secret keys or credentials to GitHub.
- Public deployments should implement suitable access controls and usage safeguards.

## 👨‍💻 Developer

**Project:** Nexa AI  
**GitHub:** [Izato-07/nexa-ai](https://github.com/Izato-07/nexa-ai)

## 📜 Disclaimer

Nexa AI is an educational project developed for learning and internship purposes. Its functionality depends on the availability and usage limits of the Groq API.
