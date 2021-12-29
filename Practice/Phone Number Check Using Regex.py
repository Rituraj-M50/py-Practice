import re

Phone = input("Enter the Phone No:")
if re.match('^[1-9][0-9]{9}$', Phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
