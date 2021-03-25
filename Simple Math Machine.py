pos, neg, zero, avg, mn, mx = 0, 0, 0, 0, 9223372036854775807, -9223372036854775807 

r = float(input("Welcome to the number counter program.\nEnter the total number of inputs you want to type in: "))
print("Now enter the numbers one-by-one, and let me do some mathematical magic on them :D")
for i in range(int(r)):
    print("Enter number ", i+1, ": ", end="")
    x = float(input())
    avg += x
    if x > 0:
        pos+= 1
    if x < 0:
        neg += 1
    if x == 0 :
        zero += 1
    if x > mx:
        mx = x
    if x < mn:
        mn = x
avg /= r
print("There are", pos, "Positive numbers.")
print("There are", neg, "Negative numbers.")
print("There are", zero, "Zeros.")
print("The average of the entered numbers is: ", avg)
print("The minimum of the entered numbers is: ", mn)
print("The maximum of the entered numbers is: ", mx)