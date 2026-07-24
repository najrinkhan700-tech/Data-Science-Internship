"""
operators are symbols used to perform some calculations
types:
1. arithmetic operators
+   a+b
-   a-b
*   a*b  asterisk
/   a/b
//  a//b   floor division
%   a%b     moduls
**  a**b    exponention
"""
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

"""
2. Comparision
used to compare values

==  ,a == b
>   , a > b
<   , a < b
>=  ,a >= b
<=  , a <= b
!= , a != b

"""
x = 10
y = 1
print(x == y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x != y)

"""
Logical operators:
and ->  x > y and x > z
or  ->  x > y or x > z
not ->  not x > y
"""

x = 20
y = 5
z = 25

print(x > y and x < z)

print(x > y or x > z)

print(not x > y)

"""
Identity operators
used to check identity of two obeject or variable
is 
is not
x,y   ,   x is y,   x is not y
"""
x = 10
y = 10
print(x is not y)

"""
Membership operator
in
not in 
"""

name = ["Rahul","Sonu","Neha","Rupali"]
fr = "Sonu"
print(fr not in name)

"""

bitwise operator
1,0
& (and)
| (or)
~ (not)
<< bitwise left shift
>> bitwise right shift
A   B   &   |   ~A
1   1   1   1   0
1   0   0   1   0
0   1   0   1   1
0   0   0   0   1
"""
a = 10
b = 2
print(a<<b)
print(a>>b)