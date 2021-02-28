def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
print("Welcome to the Factorial Calculator!\nHow does it work?\nEnter any number in "
+ "order to show a table containing the factorial of every number up to your input.\nWARNING: The higher you go, "
+ "the higher the input, the longer the calculation process will take")
x = int(input("Enter a number: "))

for n in range(1, x + 1): # testing
    print(n, factorialFun(n))