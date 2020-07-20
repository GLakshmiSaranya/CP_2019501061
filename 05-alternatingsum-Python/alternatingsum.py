# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.

def fun_alternatingsum(a):
	alternate_sum = 0
	count = 1

	for i in a:
		if count % 2 == 0:
			alternate_sum -= i
		else:
			alternate_sum += i
		count += 1
	return alternate_sum