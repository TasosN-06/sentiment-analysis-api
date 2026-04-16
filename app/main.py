from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI(title="Sentiment Analysis API")

class TextInput(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_sentiment(input: TextInput):
    result = predict(input.text)
    return {
        "text": input.text,
        "label": result["label"],
        "score": result["score"]
    }