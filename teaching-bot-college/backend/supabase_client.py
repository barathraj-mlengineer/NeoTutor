from supabase import create_client
from utils.config import load_api_key

url = load_api_key("SUPABASE_URL")
key = load_api_key("SUPABASE_KEY")
supabase = create_client(url, key)

def save_lesson(topic, content):
    data = {"topic": topic, "content": content}
    supabase.table("lessons").insert(data).execute()
