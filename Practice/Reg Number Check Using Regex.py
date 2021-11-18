import re

Reg_No = input("Enter the Reg No:")
if re.match('^([0-9][1-9])|([1-9][0-9])[A-Z]{3}[0-9]{4}$', Reg_No):
    print("Valid VIT Reg No")
else:
    print("Invalid VIT Reg No")
