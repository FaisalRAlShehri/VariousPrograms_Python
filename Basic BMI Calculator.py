def bmi(weight, height):
    return weight / height ** 2

weight = float(input("Enter your Weight (In Kilograms): "))
height = float(input("Enter your Height (In Meters): "))
print(bmi(weight, height))