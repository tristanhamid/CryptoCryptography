class User:
    def  __init__(self, first_name, last_name, wallet_address):
        self.first_name = first_name
        self.last_name = last_name
        self.wallet_address = wallet_address

def is_current_user(y_or_no_user):
    if y_or_no_user == "Y":
        return True
    elif y_or_no_user == "N":
        return False
    else:
        print("Error. Please try again.")
        exit()

