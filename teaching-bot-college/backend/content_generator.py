import requests
from utils.config import load_api_key

def generate_content(topic):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-8b-8192",  # Make sure this is a valid Groq model
        "messages": [
            {"role": "system", "content": "You are a helpful tutor."},
            {"role": "user", "content": f"Explain the topic '{topic}' in simple language for college students."}
        ],
        "temperature": 0.7
    }

    try:
        res = requests.post(url, headers=headers, json=payload, timeout=10)
        res.raise_for_status()  # Raise HTTPError for bad HTTP status

        data = res.json()

        if "choices" not in data:
            raise ValueError(f"Unexpected response format: {data}")

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")

    except ValueError as e:
        raise RuntimeError(f"Response parsing failed: {e}")
