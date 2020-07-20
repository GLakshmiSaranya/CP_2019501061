# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	# for i in L:
	# 	for j in i:
	# 		if L.count(j) > 1:
	# 			return True
	# return False

	L1 = set(L)
	if len(L) == len(L1):
		return False
	return True
	pass