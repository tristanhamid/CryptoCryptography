from datetime import datetime, timezone
from core.blockchain import get_blockchain_data

class User:
    def __init__(self, id, first_name, last_name, message, btc_price, supply, block, hash_rate, utc_time):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.message = message
        self.btc_price = btc_price
        self.supply = supply
        self.block = block
        self.hash_rate = hash_rate
        self.utc_time = utc_time

#Imaginary home page
print("Welcome to the CryptoCryptography Project!\n")

# Step 1: Request User Information
# This assumse information that would be gathered at checkout
# first_name = input("What is your first name?")
# last name = input("What is your last name?")
# message = input("What is your wallet address or personalized message you would like displayed on the coin?\n")

# Step 2: Get Blockchain information
btc_price = get_blockchain_data()[0]
supply = get_blockchain_data()[1]
block = get_blockchain_data()[2]
hash_rate = get_blockchain_data()[3]
utc_time = get_blockchain_data()[4]

print("Price (USD): ",btc_price)
print("Supply (BTC): ", supply)
print("Block height: ", block)
print("Hash Rate: ", hash_rate)
print("Timestamp (UTC): ", utc_time)

# Step 3: Create a cryptographic hash to authenticate this user transaction





