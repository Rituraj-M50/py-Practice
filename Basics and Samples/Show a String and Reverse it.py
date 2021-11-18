string = input("Enter a string:")
length = len(string)
i=0
for a in range(-1,(-length-1),-1):
    print(string[i],"\t",string[a])
    i+=1
