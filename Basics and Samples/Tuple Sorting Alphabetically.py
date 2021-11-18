def SortTuple(tup): 
	
	
	n = len(tup) 
	
	for i in range(n): 
		for j in range(n-i-1): 
			
			if tup[j][0] > tup[j + 1][0]: 
				tup[j], tup[j + 1] = tup[j + 1], tup[j] 
				
	return tup 
	
tup = [("Aman", 28), ("Hayat", 30), ("Prayag", 18), 
		("Nihal", 21), ("Rituraj", 17)] 
		
print(SortTuple(tup)) 
