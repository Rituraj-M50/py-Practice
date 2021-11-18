def Merge(dict1, dict2): 
	res = {**dict1, **dict2} 
	return res
	
dict1 = {'a': 2, 'b': 4} 
dict2 = {'d': 6, 'c': 8} 
result = Merge(dict1, dict2) 
print(result) 
