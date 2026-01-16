from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# =============================
# LOAD ML MODELS
# =============================

# Load emotion detection model
with open("models/emotion_model.pkl", "rb") as f:
    emotion_model = pickle.load(f)

# Load engagement prediction model
with open("models/engagement_model.pkl", "rb") as f:
    engagement_model = pickle.load(f)

# Emotion to numeric mapping (must match training)
emotion_map = {
    "happy": 0,
    "sad": 1,
    "angry": 2,
    "neutral": 3
}

# =============================
# FASTAPI APP
# =============================

app = FastAPI(
    title="Emotion-Aware Adaptive Conversational AI",
    description="Detects user emotion, predicts engagement, and adapts responses",
    version="1.0"
)

# =============================
# REQUEST MODEL
# =============================

class ChatInput(BaseModel):
    message: str

# =============================
# ADAPTIVE RESPONSE LOGIC
# =============================

def adaptive_response(emotion: str, engagement: str) -> str:
    if engagement == "Low":
        if emotion in ["angry", "sad"]:
            return "I sense some frustration. Want me to guide you step by step?"
        else:
            return "This seems a bit tricky. Should I help you out?"

    elif engagement == "Medium":
        return "You're doing okay. Let me know if you want some tips."

    else:  # High engagement
        return "Great! Let's keep going 👍"

# =============================
# ROUTES
# =============================

@app.get("/")
def root():
    return {
        "status": "Backend running successfully",
        "models_loaded": True
    }

@app.post("/analyze")
def analyze_message(data: ChatInput):
    # -------- 1. Emotion Prediction --------
    emotion = emotion_model.predict([data.message])[0]

    # -------- 2. Feature Engineering --------
    emotion_code = emotion_map.get(emotion, 3)
    message_length = len(data.message)
    response_gap = 2      # simulated (seconds)
    emoji_used = 0        # simulated (0 = no emoji)

    features = [[
        emotion_code,
        message_length,
        response_gap,
        emoji_used
    ]]

    # -------- 3. Engagement Prediction --------
    engagement = engagement_model.predict(features)[0]

    # -------- 4. Adaptive Response --------
    response_text = adaptive_response(emotion, engagement)

    # -------- 5. Final Output --------
    return {
        "emotion": emotion,
        "engagement": engagement,
        "adaptive_response": response_text,
        "debug": {
            "message_length": message_length,
            "response_gap": response_gap,
            "emoji_used": emoji_used
        }
    }
