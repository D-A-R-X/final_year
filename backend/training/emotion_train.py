import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# -----------------------------
# SAMPLE EMOTION DATASET
# -----------------------------
data = {
    "message": [
        "I am so happy today!",
        "This makes me sad",
        "I am angry about this",
        "Feeling neutral",
        "Great day ahead",
        "Feeling down",
        "This is frustrating",
        "Nothing special",
        "Excited for the weekend",
        "Disappointed with results"
    ],
    "emotion": ["happy", "sad", "angry", "neutral", "happy", "sad", "angry", "neutral", "happy", "sad"]
}

df = pd.DataFrame(data)

X = df["message"]
y = df["emotion"]

# Create pipeline
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train model
pipeline.fit(X, y)

# Save model
with open("models/emotion_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Emotion model trained and saved successfully.")
