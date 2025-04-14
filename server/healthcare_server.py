import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"  

def call_llama(prompt):
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful AI doctor assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 300,
        "top_p": 0.9,
    }

    res = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=payload)

    # This line will throw error if the status is not 200
    res.raise_for_status()

    return res.json()["choices"][0]["message"]["content"].strip()


@app.route('/api/analyze-symptoms', methods=['POST'])
def analyze_symptoms():
    try:
        symptoms = request.json.get("symptoms", "")

        triage = call_llama(f"Triage the following symptoms: {symptoms}")
        diagnosis = call_llama(f"Suggest possible medical conditions for: {symptoms}")
        education = call_llama(f"Provide patient education related to: {symptoms}")
        referral = call_llama(f"What medical actions should be taken for: {symptoms}")

        return jsonify({
            "analysis": {
                "triage": triage,
                "diagnosis": diagnosis,
                "education": education,
                "referral": referral
            }
        })
    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=3000, debug=True)
