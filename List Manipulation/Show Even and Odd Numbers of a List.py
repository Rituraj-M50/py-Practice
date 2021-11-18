list1 = [10, 21, 4, 45, 66, 93, 11] 
##Using Lambda()func. 
even_no = list(filter(lambda x: (x % 2 == 0), list1)) 
print("Even numbers in the list: ", even_no)

odd_no = list(filter(lambda x: (x % 2 != 0), list1)) 
print("Odd numbers in the list: ", odd_no) 

