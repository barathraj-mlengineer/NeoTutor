import requests
from utils.config import load_api_key

def generate_content(topic):
    api_key = load_api_key("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": f"Explain the topic '{topic}' in simple language for college students."}],
        "temperature": 0.7
    }
    res = requests.post(url, headers=headers, json=payload)
    return res.json()['choices'][0]['message']['content']
