from core.userprofile import *

#Imaginary home page
print("Welcome to the CryptoCryptography Project!\n")

# Step 1: Verify if user has an account
# Starting with simple CLI to detrmine whether user has an account or not. 
y_or_n_user = input("Do you have a user account? Y or N\n").upper()

is_user_bool = is_current_user(y_or_n_user)


# If user, prompt for username and password. Else request new user setup. 
if is_user_bool:
    print("Welcome back! Please enter your username and password to begin.")
    # username/password request and login function. database?
else:
    print("No worries! Lets get you set up with an account.")
    full_name = input("What is your first and last name?\n")
    full_name_split = full_name.split(" ")
    first_name = full_name_split[0]
    last_name = full_name_split[1]
    wallet_address = input("What is your wallet address?\n")
    new_user = User(first_name, last_name, wallet_address)
    