
from telegram_bot import send_signal
from strategy import generate_signal
from quotex_scraper import get_market_data

if __name__ == "__main__":
    print("Signal bot started...")
    data = get_market_data()
    signal = generate_signal(data)
    if signal:
        send_signal(signal)
