def bmi(weight, height):
    if weight < 20 or weight > 220 or height < 1.00 or height > 2.50:
        return "The data you entered are logically incorrect"
    else:
        return weight / height ** 2

weight = float(input("Enter your Weight (In Kilograms): "))
height = float(input("Enter your Height (In Meters): "))
print(bmi(weight, height))