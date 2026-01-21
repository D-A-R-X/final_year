from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class ChatInput(BaseModel):
    message: str

with open("backend/models/emotion_model.pkl","rb") as f:
    emotion_model = pickle.load(f)

with open("backend/models/engagement_model.pkl","rb") as f:
    engagement_model = pickle.load(f)

emotion_map = {"happy":0,"sad":1,"angry":2,"neutral":3}

def adaptive_reply(emotion, engagement):
    if engagement == "Low":
        return "I sense frustration. Want help?"
    if engagement == "Medium":
        return "You're doing okay. Need guidance?"
    return "Great! Let's continue."

@app.get("/")
def root():
    return {"status":"Backend running"}

@app.post("/analyze")
def analyze(data: ChatInput):
    emotion = emotion_model.predict([data.message])[0]
    features = [[emotion_map.get(emotion,3), len(data.message), 2, 0]]
    engagement = engagement_model.predict(features)[0]

    return {
        "emotion": emotion,
        "engagement": engagement,
        "response": adaptive_reply(emotion, engagement)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
