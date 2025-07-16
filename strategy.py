import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD

def generate_signal(candles):
    df = pd.DataFrame(candles)
    df['rsi'] = RSIIndicator(close=df['close'], window=14).rsi()
    df['ema9'] = EMAIndicator(close=df['close'], window=9).ema_indicator()
    df['ema21'] = EMAIndicator(close=df['close'], window=21).ema_indicator()
    macd = MACD(close=df['close'])
    df['macd_hist'] = macd.macd_diff()

    last = df.iloc[-1]

    if last['rsi'] < 30 and last['ema9'] > last['ema21'] and last['macd_hist'] > 0:
        return "CALL"
    elif last['rsi'] > 70 and last['ema9'] < last['ema21'] and last['macd_hist'] < 0:
        return "PUT"
    return None