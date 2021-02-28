word = input("Enter the word you wish to find: ").upper()
src = input("Enter the string you wish to search through: ").upper()

found = True
start = 0
count = 0

for ch in word:
	pos = src.find(ch, start) 
	if pos < 0:
		found = False
		break
	else:
		 count+= 1
	start = pos + 1
if found:
	print("The word is mentioned in the string.\nIt is mentioned ", count, " times.")
else:
	print("The word isn't mentioned in the string.")