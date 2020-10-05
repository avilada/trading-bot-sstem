import numpy as np
import robin_stocks as rp
import time

#Login:

with open("robinhood_login.txt", "r") as f:
    login = rp.login(f.readline(), f.readline())

# Load Stock Info

stocks = rp.stocks.get_quotes("AAPL")
print(stocks)

# Logout:

rp.logout()