x = input("abc:")
if x >= '0':
    print("it's a digit")
elif (x >= "A") and (x <= "Z"):
    print("its uppercase")
elif (x >= "a") and (x <= "z"):
    print("its lowercase")
else:
    print("invalid input")
