from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

def get_live_candles(pair, tf):
    # For demo purpose: Generate dummy real data structure
    # Replace with real scraping logic from Quotex chart page
    candles = []
    base = 100 + random.uniform(-1, 1)
    for _ in range(50):
        open_ = base
        close = open_ + random.uniform(-0.5, 0.5)
        high = max(open_, close) + random.uniform(0.1, 0.3)
        low = min(open_, close) - random.uniform(0.1, 0.3)
        candles.append({
            "open": open_,
            "high": high,
            "low": low,
            "close": close,
            "volume": 1000
        })
        base += random.uniform(-0.2, 0.2)
    return candles