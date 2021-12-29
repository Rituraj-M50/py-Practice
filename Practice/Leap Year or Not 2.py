x = int(input("Enter the year :"))
if ( (x%400 == 0) or (x%4 == 0) and (x%100!=0) ):
    print("Leap year")
else:
    print("Not a Leap year")
