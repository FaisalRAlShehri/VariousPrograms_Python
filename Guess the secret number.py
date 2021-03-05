from random import randint

secret_number =  randint(0, 100)

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you between 0 & 100.|
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter the number: "))

while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter the number again: "))
print(secret_number, "Well done, muggle! You are free now.")