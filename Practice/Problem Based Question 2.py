cities = set()
m1 = set()
m2 = set()
m3 = set()
n = int(input("Enter the number of cities:"))
for i in range(n):
    a = input("Enter the city name:")
    cities.add(a)
n1 = int(input("Enter the cities visited by first emp:"))
for i in range(n1):
    b = input("Enter the city name:")
    m1.add(b)
n2 = int(input("Enter the cities visited by second emp:"))
for i in range(n2):
    c = input("Enter the city name:")
    m2.add(c)
n3 = int(input("Enter the cities visited by third emp:"))
for i in range(n3):
    d = input("Enter the city name:")
    m3.add(d)
y = m1|m2|m3
print(y)
print(cities-y)