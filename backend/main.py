from datetime import datetime, timezone
from core.blockchain import get_blockchain_data
from core.crypto_keys import *

#Imaginary home page
print("Welcome to the CryptoCryptography Project!\n")

# Step 1: Request User Information
# This assumse information that would be gathered at checkout
# first_name = input("What is your first name?")
# last name = input("What is your last name?")
# message = input("What is your wallet address or personalized message you would like displayed on the coin?\n")

# Step 2: Get Blockchain information
data = get_blockchain_data()
btc_price = data[0]
supply = data[1]
block = data[2]
hash_rate = data[3]
utc_time = data[4]

print("Price (USD): ",btc_price)
print("Supply (BTC): ", supply)
print("Block height: ", block)
print("Hash Rate: ", hash_rate)
print("Timestamp (UTC): ", utc_time)

# Step 3: Create a cryptographic hash to authenticate this user transaction
key_data = generate_key_pair()
private_key_pem = key_data[0]
private_key_str = key_data[1]
public_key_pem = key_data[2]
public_key_str = key_data[3]
# Might not need to hash if I can put public key in metadata
fingerprint = sha256_hash(public_key_pem)

