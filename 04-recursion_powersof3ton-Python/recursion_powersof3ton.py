# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

import math
def recursion_powersof3ton(n):
	# Your code goes here
	if n < 1:
		return None
	
	power_arr = []
	num = math.ceil(n - 1)
	return divisible_by_3(num, power_arr, 0)
	pass

def divisible_by_3(num, power_arr, n):
	if num < n:
		return power_arr
	
	val = 3 ** n
	if val <= num:
		power_arr.append(val)
	n += 1
	return divisible_by_3(num, power_arr, n)