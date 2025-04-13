# 🧠 Healthcare AI Assistant

A powerful AI-powered tool built with React and Flask, designed to help clinics, communities, and individuals assess symptoms and receive medical guidance instantly using LLMs.

> _“We see the world not just as it is, but as it could be.”_

---

## 🔧 Technology Stack

| Part      | Tech Used                            |
|-----------|--------------------------------------|
| Frontend  | React + Tailwind + Axios             |
| Backend   | Flask (Python) + Together.ai API     |
| AI Model  | Mixtral-8x7B via Together.ai         |
| LLM Role  | Triage, Diagnosis, Education, Referral agents |

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YGIHANA1/HEALTHCARE_AI_ASSISTANT.git
cd HEALTHCARE_AI_ASSISTANT

2️⃣ Backend Setup (Python + Flask)
🔁 Go to the backend directory:

cd server

🐍 Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

📦 Install dependencies

pip install -r requirements.txt

🔑 Create a .env file

TOGETHER_API_KEY=your_api_key_here

✅ Make sure your API key from Together.ai is working.
▶️ Start the backend server

python healthcare_server.py

Your server should run at:
http://127.0.0.1:3000/api/analyze-symptoms
3️⃣ Frontend Setup (React)
🔁 Go to the frontend directory:

cd ..

📦 Install Node packages

npm install

▶️ Run the development server

npm run dev


