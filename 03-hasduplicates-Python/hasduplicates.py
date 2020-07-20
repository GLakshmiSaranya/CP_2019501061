# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	L1 = []
	for i in L:
		for j in i:
			if j not in L1:
				L1.append(j)
			else:
				return True
	return False
	pass