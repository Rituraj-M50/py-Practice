## Python3 program to Swap first 
## and last element of a list 

## Swap function 
def swapList(newList): 
	size = len(newList) 
	
	# Swapping 
	temp = newList[0] 
	newList[0] = newList[size - 1] 
	newList[size - 1] = temp 
	
	return newList
a = input("Enter 1st Value:")
b = input("Enter 2nd Value:")
c = input("Enter 3rd Value:")
d = input("Enter 4th Value:")
	 
newList = [a, b, c, d] 
print(swapList(newList)) 
