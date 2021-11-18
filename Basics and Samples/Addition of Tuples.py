 
tuple1 = (10, 16, 8) 
tuple2 = (3, 5, 18) 
 
print("The original tuple 1 : " + str(tuple1)) 
print("The original tuple 2 : " + str(tuple2)) 

result = tuple(map(lambda i, j: i + j, tuple1, tuple2)) 

print("Resultant Tuple after Addition : " + str(result)) 
