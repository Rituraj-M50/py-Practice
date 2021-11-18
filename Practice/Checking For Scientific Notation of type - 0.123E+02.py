import re
'''Checking For Scientific Notation of type - 0.123E+02'''
a = input("Enter a number:")
print(re.match('^[-+]?[0-9][0-9]*[.][0-9]*[Ee][-+]?[0-9]*$', a))
