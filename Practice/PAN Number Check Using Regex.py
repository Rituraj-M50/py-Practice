import re

PAN = input("Enter the PAN:")
if re.match('^[A-Z]{5}[0-9]{4}[A-Z]$', PAN):
    print("Valid PAN")
else:
    print("Invalid PAN")
