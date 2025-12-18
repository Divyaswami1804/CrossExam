CrossExam 🧠⚖️

A skeptical mock interview system that challenges your answers instead of praising them.

📌 Overview

CrossExam is a mock interview web application designed to simulate real, high-pressure interviews.
Unlike friendly chatbots, CrossExam behaves like a skeptical interviewer — it questions vague answers, challenges assumptions, and forces clarity.

The system combines:

Rule-based evaluation (deterministic logic)

LLM-powered adversarial feedback (Gemini)
while keeping all scoring and verdicts under developer control.

🚀 Key Features

🔍 Rule-Based Analysis

Detects vague answers, buzzwords, missing justification, and low depth

⚔️ Adversarial Interview Feedback

Uses Gemini to argue against your answer (no praise, no sugarcoating)

📊 Deterministic Scoring Engine

Numeric scoring based on rules (not AI guesses)

🧠 Final Verdict

HIRE, BORDERLINE, or REJECT

🖥️ Clean Interview UI

Built with Streamlit for fast iteration and demos

🔌 Modular Architecture

Easy to swap AI models or extend logic

🏗️ Architecture
Streamlit (UI)
     ↓
Flask Backend (API)
     ↓
Rule-Based Logic (Evaluation & Scoring)
     ↓
Gemini API (Adversarial Feedback Only)


Important:
Gemini is used only to generate critical feedback.
All evaluation, scoring, and decisions are handled by custom Python logic.

📂 Project Structure
CrossExam/
│
├── app.py                # Streamlit frontend
├── server.py             # Flask backend
│
├── logic/
│   ├── rules.py          # Rule-based answer analysis
│   ├── scorer.py         # Scoring & verdict logic
│   └── flip.py           # Decision-flip adjustments
│
├── llm/
│   └── adversary.py      # Gemini API integration
│
└── README.md

🛠️ Tech Stack

Python

Flask – backend API

Streamlit – frontend UI

Google Gemini API – adversarial feedback generation

▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/CrossExam.git
cd CrossExam

2️⃣ Install dependencies
pip install flask streamlit requests google-generativeai

3️⃣ Add your Gemini API key

Inside llm/adversary.py, replace:

API_KEY = "YOUR_API_KEY_HERE"


⚠️ Do not commit real API keys to GitHub.

4️⃣ Start the Flask backend
python server.py

5️⃣ Start the Streamlit app (new terminal)
streamlit run app.py


Open the browser link shown by Streamlit.

🎯 Example Workflow

System asks an interview question

User submits an answer

Rule engine evaluates clarity, depth, and structure

Gemini generates adversarial critique

System calculates score and verdict

🧠 Design Philosophy

“AI assists — code decides.”

CrossExam is intentionally not a chatbot.
It is an interview evaluation system that uses AI as a tool, not as the decision-maker.

🔮 Future Improvements

Topic-specific interviews (DSA, HR, Projects)

Difficulty levels

Follow-up questions based on weak answers

Session history & progress tracking

Resume-aware questioning

⚠️ Disclaimer

This project is built for learning, demos, and interview preparation.
It is not intended to replace real interview processes.

🙌 Author

Built by Divya swami
Focused on system design, logic-first engineering, and practical learning.
