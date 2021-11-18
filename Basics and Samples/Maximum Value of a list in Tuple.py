tuple1 = [('list_1', [3, 4, 5]), ('list_2', [1, 4, 2]), ('list_3', [8, 6, 2])] 
print("The original list : " + str(tuple1))

print()

result = [(list_, max(lst)) for list_, lst in tuple1] 
print("The list Tuple Attribute Maximum Value is : " + str(result)) 
