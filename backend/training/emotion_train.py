import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

data = {
    "text": [
        "I am happy",
        "This is great",
        "I feel sad",
        "This is annoying",
        "I am angry",
        "Feeling tired",
        "Awesome work",
        "This is bad"
    ],
    "emotion": [
        "happy", "happy", "sad", "angry",
        "angry", "sad", "happy", "sad"
    ]
}

df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LinearSVC())
])

model.fit(df["text"], df["emotion"])

with open("models/emotion_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Emotion model saved")
