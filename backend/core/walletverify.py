import os
from dotenv import load_dotenv
import requests

load_dotenv()

def is_valid_address(wallet_address):
    if len(wallet_address >= 26) & len(wallet_address <= 36):
        return True
    else:
        return False
    
def wallet_balance(wallet_address):
    url = "https://api.bitcoin-balance-api.com/v1/address/"+ wallet_address + "?apikey=" + os.getenv("BITCOIN_BALANCE_API_KEY")
    response = requests.get()