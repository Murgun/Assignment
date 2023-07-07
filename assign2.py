a = 10
b = 2

print("ARITHMETIC OPERATORS")
add = a+b
sub = a-b
mul = a*b
div = a/b
print(add)
print(sub)
print(mul)
print(div)

print("COMPARISON OPERATORS")
print(a<b)
print(a>b)
print(a==b)
print(a!=b)

print("LOGICAL OPERATORS")
# And Operator
if a>0 and b>0:
    print("Numbers are greater")
else:
    print("Both are less than 0")
# Or Operator
if a > 0 or b > 0: 
    print("Both the numbers are greater than 0") 
else: 
    print("No numbers are greater than 0")
# Not Operator
if not a: 
    print("Boolean value of a is True") 
  
if not (a%3 == 0 or a%5 == 0): 
    print("10 is not divisible by either 3 or 5") 
else: 
    print("10 is divisible by either 3 or 5")

print("BITWISE OPERATORS") 
#Bitwise AND operation
print("a & b =", a & b)
 
#Bitwise OR operation
print("a | b =", a | b)
 
#Bitwise NOT operation
print("~a =", ~a)
 
#Bitwise XOR operation
print("a ^ b =", a ^ b)

print("ASSIGNMENT OPERATORS")
c = a+b
print("c=",c)
a+=b
print("a=",a)
z = 3
d = 4
z-=d
print("z=",z)
e = 6
f = 7
e%=f
print("e=",e)
g = 3
h = 4
g&=h
print("g=",g)
i = 4
j = 7
i*=j
print("i=",i)
k = 6
l = 5
k/=l
print("k=",k)

print("MEMBERSHIP OPERATOR")
str = "Shubh"
print("in","h"in str)
print("not in","S"not in str)

print("IDENTIFY OPERATOR")
print("is","Shubh"is str)
print("is not","S"is not str)


