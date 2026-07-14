# Personalized Networking Assistant

## Overview

The Personalized Networking Assistant is an AI-powered web application that helps students and professionals prepare for networking events such as conferences, hackathons, workshops, and career fairs.

The application generates personalized networking plans, provides AI-powered networking guidance, verifies information using Wikipedia, and maintains conversation and feedback history. It is built using FastAPI for the backend, Streamlit for the frontend, and Google Gemini for intelligent response generation.

---

## Features

- AI Event Copilot for personalized networking plans
- AI-powered Networking Guidance using Google Gemini
- Event Analysis using DistilBERT
- Wikipedia Fact Checker
- Conversation History with AI-generated summaries
- Feedback History with AI-powered analysis
- RESTful APIs developed using FastAPI
- Interactive user interface using Streamlit
- Unit testing using Pytest and HTTPX

---

## Technologies Used

### Backend
- Python
- FastAPI
- Google Gemini API
- Hugging Face Transformers (DistilBERT)
- SQLite
- Wikipedia API

### Frontend
- Streamlit

### Testing
- Pytest
- HTTPX
- FastAPI Swagger UI

### Tools
- Git
- GitHub
- Visual Studio Code

---

## Project Structure

```
Personalized-Networking-Assistant/
│
├── backend/
│   ├── database.py
│   ├── event_analyzer.py
│   ├── fact_checker.py
│   ├── feedback_logger.py
│   ├── history_logger.py
│   ├── main.py
│   ├── schemas.py
│   ├── services.py
│   └── topic_generator.py
│
├── frontend/
│   └── app.py
│
├── tests/
│   ├── test_api.py
│   ├── test_fact_check.py
│   ├── test_history.py
│   └── test_networking.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Personalized-Networking-Assistant.git
```

Move into the project directory

```bash
cd Personalized-Networking-Assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root and add:

```text
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## Running the Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

```bash
streamlit run frontend/app.py
```

Application URL

```
http://localhost:8501
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|-------------------------|-----------------------------------|
| GET | / | Home |
| POST | /event-copilot | Generate networking plan |
| GET | /networking-coach | AI networking guidance |
| GET | /fact-check | Wikipedia fact verification |
| GET | /history | Retrieve conversation history |
| POST | /feedback | Store user feedback |
| GET | /feedback | Retrieve feedback history |
| GET | /history-summary | AI conversation summary |
| GET | /feedback-summary | AI feedback analysis |

---

## Testing

Run all tests

```bash
pytest
```

Tested using

- Pytest
- HTTPX
- FastAPI Swagger UI

---

## Key Functionalities

- Generates personalized networking plans using Google Gemini
- Provides AI-powered networking advice
- Performs event analysis using DistilBERT
- Verifies factual information through Wikipedia
- Stores conversation history
- Stores user feedback
- Generates AI-based summaries and feedback analysis

---

## Future Enhancements

- User Authentication
- Cloud Deployment
- PostgreSQL Integration
- LinkedIn API Integration
- User Profile Management
- Multi-language Support

---

## GITHUB LINK

GitHub: https://github.com/Sereenakudari

----

## Video Demo

Video Link: https://drive.google.com/file/d/1W9FEyr-6JNocMDgHMkN9ld9lefb91iMv/view?usp=sharing