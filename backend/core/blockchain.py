import requests
from datetime import datetime, timezone

def get_blockchain_data():
    blockchain_url = "https://api.blockchain.info/stats"

    # Convert blockchain.com data to json
    response = requests.get(blockchain_url)
    response.raise_for_status()
    blockchain_json = response.json()

    # Extract data from json
    # Time
    epoch = blockchain_json.get("timestamp") / 1000                     # Convert from ms to s
    utc_now = datetime.fromtimestamp(epoch, tz=timezone.utc)
    formatted_utc = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Bitcoin Data
    long_btc_price = int(blockchain_json.get("market_price_usd"))
    btc_price = "$" + str(f"{long_btc_price:,}")
    integer_supply = int(blockchain_json.get("totalbc") / 1e8)          # Convert satoshis to BTC
    supply = str(f"{integer_supply:,}")
    block = str(blockchain_json.get("n_blocks_total") - 1)              # Minus 1 because blocks started a Block 0
    hash_rate = str(int(blockchain_json.get("hash_rate") / 1e9)) + " EH/s"
    return btc_price,supply,block,hash_rate,formatted_utc
