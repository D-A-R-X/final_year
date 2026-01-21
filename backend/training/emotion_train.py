import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = {
    "text": [
        # happy
        "I am happy", "this is great", "awesome work", "feels good",
        "nice job", "I love this", "so cool", "great experience",
        "everything is fine", "doing well",

        # sad
        "I feel sad", "this is depressing", "feeling low", "not feeling good",
        "I'm tired of this", "so dull", "this hurts", "feels bad",
        "down today", "not okay",

        # angry
        "this is annoying", "I am angry", "so frustrating", "this sucks",
        "I'm mad", "this makes me furious", "can't stand this",
        "very irritating", "hate this", "pissing me off",

        # neutral
        "okay", "fine", "hmm", "alright",
        "not sure", "maybe", "I see", "understood",
        "got it", "whatever"
    ],
    "emotion": (
        ["happy"] * 10 +
        ["sad"] * 10 +
        ["angry"] * 10 +
        ["neutral"] * 10
    )
}

df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(df["text"], df["emotion"])

with open("models/emotion_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Emotion model retrained with expanded dataset")
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
