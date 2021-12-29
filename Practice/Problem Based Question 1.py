input_string = input("Enter a list element separated by space ")
lst_s = input_string.split()
input_string1 = input("Enter a list element separated by space ")
lst_d = input_string1.split()

common_items = set(lst_s) - (set(lst_s)-set(lst_d))
only_son = set(lst_s) - set(common_items)
only_daughter = set(lst_d) - set(common_items)
print(common_items)
print(only_son)
print(only_daughter)


