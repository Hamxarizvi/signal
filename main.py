from quotex_scraper import get_live_candles
from strategy import generate_signal
from telegram_bot import send_signal
import json
import time

with open("config.json") as f:
    config = json.load(f)

print("🚀 Quotex Real-Time Signal Bot Started")

last_signals = {}

while True:
    for pair in config["pairs"]:
        for tf in config["timeframes"]:
            candles = get_live_candles(pair, tf)
            if candles:
                signal = generate_signal(candles)
                key = f"{pair}_{tf}"
                if signal and (key not in last_signals or time.time() - last_signals[key] > config["cooldown_minutes"] * 60):
                    send_signal(pair, tf, signal)
                    last_signals[key] = time.time()
    time.sleep(30)