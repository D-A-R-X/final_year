import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

data = {
    "emotion": ["happy","sad","angry","neutral","happy","sad"],
    "msg_length": [8,40,30,15,10,45],
    "gap": [1,6,5,2,1,7],
    "emoji": [1,0,0,0,1,0],
    "engagement": ["High","Low","Low","Medium","High","Low"]
}

df = pd.DataFrame(data)
emotion_map = {"happy":0,"sad":1,"angry":2,"neutral":3}
df["emotion"] = df["emotion"].map(emotion_map)

X = df.drop("engagement", axis=1)
y = df["engagement"]

model = RandomForestClassifier()
model.fit(X, y)

with open("models/engagement_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Engagement model saved")
