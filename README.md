# final_year
🧠 Emotion-Aware Adaptive Conversational AI
Using Machine Learning for User Engagement Prediction
📌 Project Overview

This project presents an AI-powered conversational system that goes beyond traditional chatbots by understanding user emotions and predicting engagement levels in real time.
Instead of responding passively, the system adapts its responses based on the detected emotional state and predicted likelihood of user disengagement, improving overall interaction quality.

The project demonstrates the practical application of Machine Learning, Natural Language Processing, and adaptive decision logic in human–computer interaction.

🎯 Problem Statement

Most existing chatbots respond uniformly to user inputs without understanding:

User emotional state

Frustration levels

Likelihood of disengagement

This leads to poor user experience, repeated inputs, and interaction drop-off.
The problem addressed in this project is how to build a conversational AI system that can adapt its behavior based on user emotion and engagement prediction.

💡 Proposed Solution

The proposed system uses a two-stage ML pipeline:

Emotion Detection Model – identifies the emotional state of the user from text input.

Engagement Prediction Model – predicts whether the user engagement level is High, Medium, or Low.

Based on these predictions, an adaptive response engine dynamically selects appropriate responses to reduce frustration and improve engagement.

🏗️ System Architecture
User Input
   ↓
Frontend (HTML / JS)
   ↓
FastAPI Backend
   ↓
Emotion Detection Model (ML)
   ↓
Engagement Prediction Model (ML)
   ↓
Adaptive Response Logic
   ↓
User Response

🤖 Machine Learning Components
1️⃣ Emotion Detection

Input: User text message

Technique: TF-IDF + Support Vector Machine (SVM)

Output: Emotion label (Happy, Sad, Angry, Neutral)

2️⃣ Engagement Prediction

Input Features:

Detected emotion

Message length

Response time gap (simulated)

Emoji usage flag (simulated)

Technique: Random Forest Classifier

Output: Engagement level (High / Medium / Low)

🔄 Adaptive Response Logic

Based on ML predictions:

Low Engagement + Negative Emotion → calming or guiding response

Medium Engagement → supportive response

High Engagement → encouraging response

This logic enables adaptive conversational behavior, which is the core innovation of the project.

🛠️ Technologies Used

Programming Language: Python

Backend Framework: FastAPI

Machine Learning: Scikit-learn

Frontend: HTML, CSS, JavaScript

Deployment (Free Tier):

Backend: Render / Railway

Frontend: Vercel

🚀 How to Run the Project Locally
Backend Setup
cd backend
pip install -r requirements.txt
python training/emotion_train.py
python training/engagement_train.py
python -m uvicorn app:app --reload


Backend will run at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

Frontend Setup

Open frontend/index.html in a browser
(or deploy frontend folder using Vercel).

📊 Sample Output
{
  "emotion": "angry",
  "engagement": "Low",
  "response": "I sense frustration. Want help?"
}

✅ Advantages

Real-time emotion-aware responses

Predicts user disengagement proactively

Adaptive conversational behavior

Modular and extensible architecture

Suitable for real-world applications

🔭 Future Scope

Voice-based emotion detection

GIFs and media-based adaptive responses

Long-term user behavior learning

Multilingual support

Deep learning-based emotion models

🎓 Academic Relevance

This project demonstrates:

Supervised Machine Learning

Feature engineering

Real-time ML inference

Adaptive decision systems

Practical AI deployment

It is suitable for final-year AI & ML project evaluation.

👥 Team

Team Member 1: TBD

Team Member 2: TBD

📜 License

This project is developed for academic and educational purposes.