tuple1 = (10, 8, 20) 
tuple2 = (2, 5, 18) 

print("The original tuple 1 : " + str(tuple1)) 
print("The original tuple 2 : " + str(tuple2)) 

result = tuple(map(lambda i, j: i - j, tuple1, tuple2)) 
 
print("Resultant Tuple after Subtraction : " + str(result)) 
