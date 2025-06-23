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
