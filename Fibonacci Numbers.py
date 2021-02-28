# They are a sequence of integer numbers built using a very simple rule:
# every subsequent number is the sum of the two preceding numbers (Fib i = Fib i-1 + Fib i-2)

print("Welcome to the Fibonacci Numbers Calculator!\nHow does it work?\nEnter any number in "
+ "order to show a table containing the Fibonacci number of every number up to your input.\nWARNING: The higher you go, "
+ "the higher the input, the longer the calculation process will take.")
x = int(input("Enter a number: "))

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, x + 1): # testing
    print(n, "->", fib(n))