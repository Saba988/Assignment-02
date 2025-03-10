## **Q3 (Monday 2-5)** - **Assignment** **(Class 02)**

# **Operators In Python**

#Arithmetic operators
x:int=3
y:int=2
print("x + y = ",x+y)    #Addition
print("x - y = ",x-y)    #Subtraction
print("x * y = ",x*y)    #Multiplication
print("x / y = ",x/y)    #Division
print("x % y = ",x%y)    #Modulus
print("x **y = ",x**y)   #Exponentiation
print("x //y     = ",x//y)   #Floor Division

#Assignment operators
x:int = 7
print("Assignment: ",x)

x += 3
print("Addition Assignment: ",x)

x -= 3
print("Subtraction Assignment: ",x)

x*= 3
print("Multiplication Assignment: ",x)

x /= 3
print("Division Assignment: ",x)

x%=3
print("Modulus Assignment: ",x)

x**=3
print("Exponentiation Assignment: ",x)

x //= 3
print("Floor Division Assignment: ",x)

#Comparison Operators
x: int = 4
y: int = 9

print("x == y = ", x == y)    #Equal to
print("x != y = ", x != y)    #Not Equal to
print("x > y  = ", x > y)     #Greater than
print("x < y  = ", x < y)     #Less than
print("x >= y = ", x >= y)    #Greater than or equal to
print("x <= y = ", x <= y)    #Less than or equal to

#Logical Operators
x: bool = True
y: bool = False

print("x and y = ", x and y)  # And
print("x or y  = ", x or y)   # Or
print("not x   = ", not x)    # Not

#Identity Operators
a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c     =  ",a is c)
print("a is b     =  ",a is b)
print("a == b     =  ", a == b)
print("a is not b =  ", a is not b)
print("\n")
print("Checking Memory Addresses")
print("\n")

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))

#Membership Operators
my_list: list = [1, 2, 3, 4, 5,10,98]

print("my_list           = ", my_list)
print("3 in my_list      = ", 98 in my_list)
print("10 not in my_list = ", 10 not in my_list)

print("\n")

my_string: str = "Mission Learning Operators"

print("my_string                 = ", my_string)
print("'O' in my_string          = ", 'L' in my_string)
print("'Hello' not in my_string  = ", 'python' not in my_string)

#Bitwise Operators
a: int = 8  # Binary: 1000
b: int = ~a  # b is now -9 (binary: 0111, but in two's complement form)
print("b = ", b)
