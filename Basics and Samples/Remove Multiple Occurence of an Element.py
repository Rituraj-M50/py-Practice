
##Using list comprehension + set() + count()  
list1 = [(3, 6, 4), (4, 6, 5), (3, 6, 4), (3, 6, 4), (4, 5, 1), (6, 7, 0)] 
 
print("The original list : " + str(list1)) 
res = list(set([ele for ele in list1 if not list1.count(ele) > 1]))

print("All the non Duplicate from list are : " + str(res)) 
