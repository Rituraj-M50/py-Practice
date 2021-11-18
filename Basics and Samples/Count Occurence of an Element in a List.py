from collections import Counter 
##Required List 
l = [1, 1, 2, 2, 4, 3, 3, 4, 4, 5, 5, 4]
x = 4
d = Counter(l) 
print('{} has occurred {} times'.format(x, d[x])) 
