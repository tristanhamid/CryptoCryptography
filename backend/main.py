from core.userprofile import *
from core.walletverify import *

class User:
    def __init__(self, id, btc_price, message, supply, block, hash_rate, utc_time):
        self.id = id
        self.btc_price = btc_price
        self.message = message
        self.supply = supply
        self.block = block
        self.hash_rate = hash_rate
        self.utc_time = utc_time

#Imaginary home page
print("Welcome to the CryptoCryptography Project!\n")

# Step 1: Request User Information
# This assumse information that would be gathered at checkout

new_user.message = input("What is your wallet address or personalized message you would like displayed on the coin?")
print(newuser.message)

# Step 2: Check bitcoin account balance based on wallet address
wallet_address = input("What is your wallet address")

