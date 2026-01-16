import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# SAMPLE ENGAGEMENT DATASET
# -----------------------------
data = {
    "emotion": ["happy", "sad", "angry", "neutral", "happy", "sad", "angry", "neutral"],
    "msg_length": [10, 35, 28, 15, 8, 42, 30, 18],
    "response_gap": [1, 5, 6, 2, 1, 7, 5, 3],
    "emoji_used": [1, 0, 0, 0, 1, 0, 0, 0],
    "engagement": ["High", "Low", "Low", "Medium", "High", "Low", "Low", "Medium"]
}

df = pd.DataFrame(data)

# Encode emotion as numbers
emotion_map = {"happy": 0, "sad": 1, "angry": 2, "neutral": 3}
df["emotion"] = df["emotion"].map(emotion_map)

X = df.drop("engagement", axis=1)
y = df["engagement"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open("models/engagement_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Engagement model trained and saved successfully.")
