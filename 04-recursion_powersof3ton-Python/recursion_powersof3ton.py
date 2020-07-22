# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

power_arr = []

def recursion_powersof3ton(n):
	# Your code goes here
	if n < 1:
		if len(power_arr) == 0:
			return None
		arr = power_arr.sort()
		power_arr = []
		return arr

	if divisible_by_3(n):
		power_arr.append(n)
	return recursion_powersof3ton(round(n))
	pass

def divisible_by_3(n):
	if n == 1 or n == 3:
		return True
	elif n % 3 > 0:
		return False
	return divisible_by_3(n / 3)