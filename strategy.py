
def generate_signal(data):
    # Dummy strategy: Buy if last candle is green, sell if red
    if not data:
        return None
    last_candle = data[-1]
    if last_candle["close"] > last_candle["open"]:
        return "🔼 Buy Signal"
    else:
        return "🔽 Sell Signal"
