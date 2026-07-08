# Personalized Networking Assistant

## Project Overview

The Personalized Networking Assistant is an AI-powered web application developed to help students and professionals prepare for networking events such as conferences, hackathons, seminars, workshops, and career fairs. The application generates personalized networking guidance, provides conversation suggestions, answers networking-related questions, verifies factual information using Wikipedia, and maintains conversation history for future reference.

The project is built using FastAPI for the backend, Streamlit for the frontend, SQLite for data storage, Hugging Face Transformers for event analysis, Google Gemini for AI-powered responses, and the Wikipedia API for fact verification.

---

## Features

- Generate personalized networking plans based on event descriptions.
- Receive AI-powered networking advice through an interactive networking coach.
- Verify topics using the Wikipedia API.
- Store and retrieve conversation history.
- Record user feedback.
- Download generated networking plans.
- RESTful API built using FastAPI.
- Interactive web interface developed using Streamlit.

---

## Technologies Used

### Frontend
- Streamlit

### Backend
- FastAPI
- Python

### Artificial Intelligence
- Google Gemini API
- Hugging Face Transformers
- DistilBERT

### Database
- SQLite

### APIs
- Wikipedia API

### Testing
- Pytest
- HTTPX

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## Project Structure

```
Personalized-Networking-Assistant
│
├── backend
│   ├── database.py
│   ├── services.py
│   ├── main.py
│   ├── event_analyzer.py
│   ├── topic_generator.py
│   ├── fact_checker.py
│   └── schemas.py
│
├── frontend
│   └── app.py
│
├── tests
│   ├── test_api.py
│   ├── test_fact_check.py
│   ├── test_history.py
│   └── test_networking.py
│
├── networking.db
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Personalized-Networking-Assistant.git

cd Personalized-Networking-Assistant
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root directory and add your Gemini API key.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Backend

Start the FastAPI server using:

```bash
uvicorn backend.main:app --reload
```

The backend will be available at:

```
http://127.0.0.1:8000
```

API documentation can be accessed at:

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Start the Streamlit application using:

```bash
streamlit run frontend/app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home endpoint |
| POST | `/event-copilot` | Generate a personalized networking plan |
| GET | `/networking-coach` | Get AI-powered networking advice |
| GET | `/fact-check` | Verify information using Wikipedia |
| GET | `/history` | Retrieve conversation history |
| POST | `/feedback` | Save user feedback |
| GET | `/feedback` | Retrieve user feedback |

---

## Testing

Unit testing was performed using **Pytest**, while API endpoint validation was completed using **HTTPX**.

Run all tests using:

```bash
pytest -v
```

All test cases passed successfully for:

- Event Copilot API
- Networking Coach API
- Fact Checker API
- Conversation History API

---

## Application Workflow

1. The user provides an event description.
2. The application analyzes the event and user input.
3. Google Gemini generates a personalized networking plan.
4. Users can ask networking-related questions through the Networking Coach.
5. Topics can be verified using the Wikipedia API.
6. Generated responses are stored in the SQLite database.
7. Users can view previous conversations and submit feedback.

---

## Future Enhancements

- User authentication and profile management.
- Integration with LinkedIn APIs.
- Event recommendation based on user interests.
- Cloud deployment for public access.
- Enhanced AI models for personalized networking recommendations.

---

## GitHub Repository

Repository Link:

```
https://github.com/Sereenakudari/Personalized-Networking-Assistant
```

---

## Demonstration

Local Deployment:

```
Frontend:
http://localhost:8501

Backend:
http://127.0.0.1:8000

Swagger Documentation:
http://127.0.0.1:8000/docs
```
---
Here we are adding the Demo link
------
https://drive.google.com/file/d/1TX-z8Yh5Qbq7WsRuFFqTGv_walsr3h90/view?usp=sharing

---------

Streamlit-app-link
-------
https://laughing-space-meme-694g9xr96wwq3r5pp.github.dev/
-------

## License

This project was developed as part of the SmartBridge AI Internship Program for educational and learning purposes.