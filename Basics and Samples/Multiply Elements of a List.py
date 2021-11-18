##Using lambda() func.
from functools import reduce
user_input = input("Enter 1st Number:")
val = int(user_input)

user_input2 = input("Enter 2nd Number:")
val2 = int(user_input2)

user_input3 = input("Enter 3rd Number:")
val3 = int(user_input3)

list1 = [val, val2, val3]
result1 = reduce((lambda x, y: x * y), list1) 
print(result1) 

