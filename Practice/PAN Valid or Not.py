P = input("Enter your PAN Number :")
X = P[0:5]
Y = P[5:9]
Z = P[9:10]
if len(P) == 10:
    if X.isalpha() == True and Y.isdigit() == True and Z.isalpha() == True:
        print("PAN is Valid")
    else:
        print("Invalid PAN")
else:
    print("Invalid PAN")
