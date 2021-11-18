x = int(input("Enter a number :"))
y = False
while x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            y = True
    break
if y:
    print(x, "is not a prime number")
else:
    print(x, "is a prime number")