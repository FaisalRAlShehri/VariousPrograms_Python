str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# this is what we're going to do with both strings:
# - remove spaces
# - change all letters to upper case
# - convert into list
# - sort the list
# - join list's elements into string
# and finally, compare both strings

in1 = ''.join(sorted(list(str1.upper().replace(' ',''))))
in2 = ''.join(sorted(list(str2.upper().replace(' ',''))))
if len(in1) > 0 and in1 == in2:
	print("The entered strings are Anagrams")
else:
	print("The entered strings are not anagrams")
