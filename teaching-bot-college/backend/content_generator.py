import requests
from utils.config import load_api_key

def generate_content(topic):
    api_key ="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"  # Or hardcode for now if needed
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",  # ✅ Valid Groq model
        "messages": [
            {"role": "system", "content": "You are a helpful tutor."},
            {"role": "user", "content": f"Explain the topic '{topic}' in simple language for college students."}
        ],
        "temperature": 0.7
    }

    try:
        res = requests.post(url, headers=headers, json=payload, timeout=10)

        # 🔍 Check if response is JSON and has the right structure
        try:
            data = res.json()
        except Exception:
            raise RuntimeError(f"❌ Invalid JSON response: {res.text}")

        if res.status_code != 200:
            error_message = data.get("error", {}).get("message", res.text)
            raise RuntimeError(f"❌ API Error {res.status_code}: {error_message}")

        if "choices" not in data:
            raise RuntimeError(f"❌ Missing 'choices' key in response: {data}")

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"❌ Request failed: {e}")
