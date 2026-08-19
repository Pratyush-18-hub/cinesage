# 🎬 CineSage

**CineSage** is an AI-powered **Information Extraction and Summarization** application built with **Python, Streamlit, LangChain, and Groq**.

It takes a paragraph as input and uses an LLM to identify the important information, determine the type of content, extract relevant entities and facts, and generate a concise summary.

## ✨ Features

* 🤖 AI-powered information extraction
* 📝 Automatic paragraph summarization
* 🔍 Content type identification
* 👤 People and character extraction
* 🏢 Organization extraction
* 📍 Location extraction
* 📅 Date and time extraction
* 📊 Numbers and statistics extraction
* 🎬 Domain-specific information extraction
* 📰 Supports content such as:

  * Movies / TV Shows
  * Books
  * News
  * People
  * Products
  * Events
  * Jobs
  * Places
  * General content

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — Web UI
* **LangChain** — Prompt management and LLM integration
* **Groq** — LLM inference
* **GPT-OSS 120B** — Language model
* **python-dotenv** — Environment variable management
* **Pydantic** — Structured output validation in the core implementation

## 📂 Project Structure

```text
cinesage/
│
├── core.py          # Core information extraction logic
├── uicore.py        # Streamlit user interface
├── requirements.txt # Python dependencies
├── .gitignore       # Ignored files and secrets
└── .env             # API key configuration (not committed)
```

## ⚙️ How It Works

The application follows this basic pipeline:

```text
User enters a paragraph
        ↓
Streamlit UI
        ↓
ChatPromptTemplate
        ↓
Groq LLM
        ↓
Information Extraction
        ↓
Summary + Key Information
        ↓
Displayed in Streamlit
```

The application instructs the model to extract information **only from the supplied paragraph** and avoid inventing information.

If a relevant field is not present in the paragraph, the model is instructed to return **"Not mentioned"**.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pratyush-18-hub/cinesage.git
cd cinesage
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

**Never commit your `.env` file or expose your API key publicly.**

The project already includes `.env` in `.gitignore`.

## ▶️ Run the Application

Run the Streamlit interface with:

```bash
python -m streamlit run uicore.py
```

The application will be available at:

```text
http://localhost:8501
```

## 💡 Example

### Input

```text
Christopher Nolan's Interstellar is a science-fiction film released in 2014. 
The movie stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and 
Michael Caine. The film follows Cooper, a former NASA pilot, who travels 
through a wormhole near Saturn to search for a habitable planet for humanity.
```

### Output

The application can identify information such as:

```text
CONTENT TYPE:
Movie / TV Show

TITLE / NAME:
Interstellar

SUMMARY:
Christopher Nolan's Interstellar is a science-fiction film released in 2014.
It follows Cooper, a former NASA pilot, who travels through a wormhole to
search for a habitable planet.

KEY INFORMATION:
- Date: 2014
- Location: Near Saturn
- Main Subject: Cooper
- People / Characters:
  - Matthew McConaughey
  - Anne Hathaway
  - Jessica Chastain
  - Michael Caine
- Organizations:
  - NASA
```

## 🧠 Core Implementation

The `core.py` implementation also demonstrates **structured output parsing using Pydantic**.

It defines a movie schema containing fields such as:

* Title
* Director
* Cast
* Release year
* Rating
* Summary

The response is parsed using LangChain's `PydanticOutputParser`.

## 🎯 Purpose

CineSage was created as a practical project to explore:

* Large Language Models
* Prompt engineering
* LangChain
* Structured output parsing
* Information extraction
* Text summarization
* Streamlit application development
* LLM-powered application development

## 🔮 Future Improvements

Possible future improvements include:

* [ ] Add downloadable analysis reports
* [ ] Add JSON export
* [ ] Add PDF export
* [ ] Add multiple model selection
* [ ] Add conversation history
* [ ] Improve UI design
* [ ] Add document/PDF upload
* [ ] Add batch text processing
* [ ] Deploy the application online
* [ ] Add more structured output schemas

## 👨‍💻 Author

**Pratyush Sahoo**

GitHub: [Pratyush-18-hub](https://github.com/Pratyush-18-hub)

## 📄 License

This project is intended for educational and portfolio purposes.
