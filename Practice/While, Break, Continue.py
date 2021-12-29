a = 10
while a:
    b = 0
    while b < 4:
        b += 1
        if b == 2:
            continue
        print("The Value of b is ::", b, end = ' ')
    a -= 1
    if (a == 7):
        break
    print(a, end=' \n')
    print("Printing Values")
print("I'm Done")

