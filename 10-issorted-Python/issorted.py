# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	# b = a
	
	# print("List of A")
	# for i in a:
	# 	print(i)
	
	# print("List of B")
	# for i in b:
	# 	print(i)
	
	b = a.copy()
	# print("List of A")
	# for i in a:
	# 	print(i)
	
	# print("List of B")
	# for i in b:
	# 	print(i)
	a.sort()

	if a == b:
		return True
	if a[ : : -1] == b:
		return True
	return False
	pass