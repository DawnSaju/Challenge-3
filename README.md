# Challenge-3

### CodeBeans 1.0 - Challenge 3

Importing Required Package.

```python
import math
```

Defining the function with 4 paramters.

```python
def Function_1(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
```

Defining the Pillar_Coordinates function with 6 paramters.
Defining a variable named as a and assigning the First function with 4 parameters.
Defining a variable named as b and assigning the First function with 4 parameters.
Defining a variable named as c and assigning the First function with 4 parameters.
Defining a varibale named as x and assigning (a + b + c) divided by 2.

```python
def Pillar_Coordinates(x1, y1, x2, y2, x3, y3):
    a = Function_1(x1, y1, x2, y2)
    b = Function_1(x1, y1, x3, y3)
    c = Function_1(x2, y2, x3, y3)
    x = (a + b + c) / 2
    return math.sqrt(x * (x - a) * (x - b) * (x - c))
```

Declaring the Variables.

```python
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
```

Final Output.

```python
print("\nOutput: ")
print(Pillar_Coordinates(x1, y1, x2, y2, x3, y3))
```
