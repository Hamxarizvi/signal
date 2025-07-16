
import requests
import json

with open("config.json", "r") as file:
    config = json.load(file)

def send_signal(message):
    url = f"https://api.telegram.org/bot{config['telegram_token']}/sendMessage"
    payload = {
        "chat_id": config["chat_id"],
        "text": message
    }
    requests.post(url, json=payload)
