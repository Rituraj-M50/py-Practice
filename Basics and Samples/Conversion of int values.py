Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=123465
>>> type(a)
<class 'int'>
>>> print(a)
123465
>>> bin(a)
'0b11110001001001001'
>>> hex(a)
'0x1e249'
>>> oct(a)
'0o361111'
>>> x=142.56
>>> type(a)
<class 'int'>
>>> type(x)
<class 'float'>
>>> bin(x)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    bin(x)
TypeError: 'float' object cannot be interpreted as an integer
>>> hex(x)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    hex(x)
TypeError: 'float' object cannot be interpreted as an integer
>>> So Conversion can be only done with 'int' values Respectively
SyntaxError: invalid syntax
>>> 
