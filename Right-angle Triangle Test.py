# We'll try to ensure that a certain triangle is a right-angle triangle.

# We will need to make use of the Pythagorean theorem:

# c**2 = a**2 + b**2
print("Welcome to the Right-angle Triangle Tester.\nIn this program, you are requested to enter the values of the 3 sides of a triangle, labeled a, b, and c, respectively.",
"The input will then be checked if it denotes a right-angle triangle or not.")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

if(isItRightTriangle(a, b, c)):
    print("Your input denotes a right-sided triangle.")
else:
    print("Your input does not denote a right-sided triangle.")