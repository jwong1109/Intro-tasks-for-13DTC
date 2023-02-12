"""Intro task 1
Secret PIN program
"""

# Main routine
secret_pin = ""
while not secret_pin:
    secret_pin = input("Enter your secret 4-digit PIN: ")
    if secret_pin == "0456":
        print("Your secret PIN is 0456")
        break
    else:
        secret_pin = ""
        print("Wrong")
