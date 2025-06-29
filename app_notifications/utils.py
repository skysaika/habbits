import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = f"https://api.telegram.org/bot{TOKEN}"


def send_telegram_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    response = requests.post(url, json={"chat_id": chat_id, "text": text})
    return response.json()