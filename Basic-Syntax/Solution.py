# Data Types
num1 = 5
num2 = 3.14
string1 = "Hello, world!"
print(num1)
print(num2)
print(string1)

bool1 = True
bool2 = False
print(bool1)
print(bool2)

# Variables
name = "John"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")

# Operators
num3 = 10
num4 = 3
print(num3 + num4)
print(num3 - num4)
print(num3 * num4)
print(num3 / num4)
print(num3 % num4)
print(num3 ** num4)

# If else statements
num5 = 8
if num5 > 10:
    print("Num5 is greater than 10")
else:
    print("Num5 is less than or equal to 10")

# Loops
# For loop
for i in range(1, 6):
    print(i)

# While loop
j = 1
while j <= 5:
    print(j)
    j += 1

# Functions
def square(x):
    return x ** 2

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(square(5))
print(factorial(5))
