import requests
import json

with open("config.json") as f:
    config = json.load(f)

def send_signal(pair, tf, direction):
    msg = f"""
🔔 SIGNAL ALERT
Pair: {pair}
Timeframe: {tf}
Direction: {"📈 CALL" if direction == "CALL" else "📉 PUT"}
Reason: RSI + EMA + MACD Confirmed
"""
    url = f"https://api.telegram.org/bot{config['telegram_token']}/sendMessage"
    requests.post(url, json={"chat_id": config['chat_id'], "text": msg})