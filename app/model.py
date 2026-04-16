from transformers import pipeline

# Φορτώνουμε το model μία φορά στην αρχή
sentiment_model = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict(text: str) -> dict:
    result = sentiment_model(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }
