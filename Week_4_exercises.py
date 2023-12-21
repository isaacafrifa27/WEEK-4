from math import sqrt

number = 2401
result = sqrt(number)

print(f"The square root of {number} is: {result}")




from math import log2

number = 1024
result = log2(number)

print(f"The log base 2 of {number} is: {result}")



def displayTwice(value):
    print(value)
    print(value)

displayTwice("Hello")
displayTwice(123)
displayTwice([1, 2, 3])
displayTwice(3.14)



def displayTwice(value):
    """
    Prints the given value twice.

    Parameters:
    value (any): The value to be displayed.

    Returns:
    None
    """
    print(value)
    print(value)

displayTwice("Hello")
displayTwice(123)
displayTwice([1, 2, 3])
displayTwice(3.14)

help(displayTwice)



def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        max_val = a
    else:
        max_val = b
    return max_val

result1 = findMax(5, 3)
result2 = findMax(-7, 10)
result3 = findMax(0, 0)

print("Maximum of 5 and 3:", result1)
print("Maximum of -7 and 10:", result2)
print("Maximum of 0 and 0:", result3)



def multiply_values(a, b=None):
    """
    Multiplies two numeric values together.
    If called with a single argument, multiplies it by itself.

    Parameters:
    a (numeric): The first numeric value.
    b (numeric, optional): The second numeric value. Defaults to None.

    Returns:
    numeric: The result of the multiplication.
    """
    if b is None:
        return a * a
    else:
        return a * b

result1 = multiply_values(5, 3)
result2 = multiply_values(-7)
result3 = multiply_values(2.5, 4.0)

print("Multiplication of 5 and 3:", result1)
print("Square of -7:", result2)
print("Multiplication of 2.5 and 4.0:", result3)



def someFunc(x=1, y=2, z=3):
    """
    Example function with default argument values.
    """
    print("x is", x)
    print("y is", y)
    print("z is", z)

someFunc(y=2, z=3, x=1)
someFunc(z=3, x=1, y=2)
someFunc(y=2, x=1, z=3)



print("Apple", "Banana", "Orange", sep=",")
print(1, 2, 3, sep="-")
print("Red", "Green", "Blue", sep=" | ")
print("January", "February", "March", sep="/")



def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

result1 = calcAve(5, 10, 15)
result2 = calcAve(2, 4, 6, 8, 10)
result3 = calcAve(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Average of 5, 10, 15:", result1)
print("Average of 2, 4, 6, 8, 10:", result2)
print("Average of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:", result3)



import math

hypot = lambda a, b: math.sqrt(a * a + b * b)


print("Data type of hypot:", type(hypot))



to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60

result1 = to_seconds(0, 2)
result2 = to_seconds(2, 0)
result3 = to_seconds(1, 30)

print("to_seconds(0, 2):", result1)
print("to_seconds(2, 0):", result2)
print("to_seconds(1, 30):", result3)



to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60

result1 = to_seconds(1)
result2 = to_seconds(2)

print("to_seconds(1):", result1)
print("to_seconds(2):", result2)
