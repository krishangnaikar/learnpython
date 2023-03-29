import math

# Exercise 1: Handling Built-in Exceptions

def divide_numbers(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def open_file(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    return file

# Exercise 2: Raising Custom Exceptions

class NegativeNumberError(Exception):
    pass

def calculate_square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number")
    return math.sqrt(x)

class KeyNotFoundError(Exception):
    pass

def find_key(d, k):
    if type(d) != dict:
        raise InvalidDataTypeError("Input is not a dictionary")
    if k not in d:
        raise KeyNotFoundError("Key not found")
    return d[k]

# Exercise 3: Handling Custom Exceptions

def get_user_input():
    try:
        num = int(input("Enter a number between 1 and 10: "))
        if num < 1 or num > 10:
            raise ValueError("Number must be between 1 and 10")
        return num
    except ValueError:
        raise ValueError("Invalid input")

def square_root_program():
    try:
        num = get_user_input()
        result = calculate_square_root(num)
        print("The square root of", num, "is", result)
    except ValueError as e:
        print("Error:", e)
    except NegativeNumberError as e:
        print("Error:", e)

def file_program():
    try:
        filename = input("Enter a file name: ")
        file = open_file(filename)
        # do something with file
    except FileNotFoundError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

# Bonus Exercise: More Custom Exceptions

class InvalidDataTypeError(Exception):
    pass

def check_string(input_str):
    if type(input_str) != str:
        raise InvalidDataTypeError("Input is not a string")

def check_valid_key(d, k):
    if type(d) != dict:
        raise InvalidDataTypeError("Input is not a dictionary")
    if type(k) != str:
        raise InvalidDataTypeError("Input is not a string")
    if k not in d:
        raise KeyNotFoundError("Key not found")
    return d[k]

