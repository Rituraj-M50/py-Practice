string = input("Enter a string:")
print("The", string, "in reverse order is:")
length = len(string)
for a in range(-1,(-length-1),-1):
    print(string[a])
