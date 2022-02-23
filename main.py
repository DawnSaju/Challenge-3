# Importing Required Package.
import math

# Defining the function with 4 paramters.
def Function_1(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Defining the Pillar_Coordinates function with 6 paramters.
def Pillar_Coordinates(x1, y1, x2, y2, x3, y3):
    # Defining a variable named as a and assigning the First function with 4 parameters.
    a = Function_1(x1, y1, x2, y2)
    # Defining a variable named as b and assigning the First function with 4 parameters.
    b = Function_1(x1, y1, x3, y3)
    # Defining a variable named as c and assigning the First function with 4 parameters.
    c = Function_1(x2, y2, x3, y3)
    x = (a + b + c) / 2
    return math.sqrt(x * (x - a) * (x - b) * (x - c))

# Declaring the Variables.
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

# Final Output.
print("\nOutput: ")
print(Pillar_Coordinates(x1, y1, x2, y2, x3, y3))
