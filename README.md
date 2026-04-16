#  🤖  Sentiment Analysis API

A production-ready REST API for sentiment analysis, built with **FastAPI** and served via **Docker**.

## 🛠️ Tech Stack

- **FastAPI** — Modern Python web framework
- **HuggingFace Transformers** — distilbert-base-uncased-finetuned-sst-2-english
- **Docker & Docker Compose** — Containerized deployment
- **Uvicorn** — ASGI server

## 🚀 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Run the API

`ash
docker-compose up --build
`

The API will be available at http://localhost:8000

## 📡 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /predict | Predict sentiment |

### Example Request & Response

`json
POST /predict
{"text": "I love this so much!"}

Response:
{"text": "I love this so much!", "label": "POSITIVE", "score": 0.9999}
`

## 📖 Interactive Docs

Swagger UI available at: http://localhost:8000/docs

## 👤 Author

Made by Tasos Nikolopoulos — learning Docker as an AI Engineer ??
