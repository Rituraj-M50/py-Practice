hrs = int(input("enter hours :"))
mn = int(input("enter minutes :"))
x = 0
if mn <= 60:
    if hrs > 7:
        print("invalid input")
    elif hrs < 5:
        x = x + hrs * 50 + mn
        print(x)
    else:
        x = 200
        hrs = hrs - 5
        x = x + hrs * 50 + mn
        print(x)
else:
    print("invalid statement")

        
    
