import numpy as np
import robin_stocks as r
import time

## username/password for account
with open('login_trading_bot.txt', 'r') as f:
    login = r.login(f.readline(), f.readline())

#TODO: Access portfolio / holdings. Load profile?
holdings = r.build_holdings()
portfolio = r.profiles.load_portfolio_profile()
account_profile = r.profiles.load_account_profile()






## Close account
r.logout()