Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=12+30j
>>> type(a)
<class 'complex'>
>>> print(a)
(12+30j)
>>> a.real
12.0
>>> a.imag
30.0
>>> ab=0B1212+120j
SyntaxError: invalid syntax
>>> ac=0b1212+100j
SyntaxError: invalid syntax
>>> a=0b1111+20j
>>> type(a)
<class 'complex'>
>>> a.real
15.0
>>> a.imag
20.0
>>> 
