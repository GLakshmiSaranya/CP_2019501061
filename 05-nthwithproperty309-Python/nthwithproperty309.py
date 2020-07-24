# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	count = 0
	start_num = 309

	while count < n:
		start_num += 1
		res = start_num ** 5
		str_res = str(res)

		for i in range(0, 10):
			if str(i) not in str_res:
				flag = False
		
		if flag:
			count += 1

	return start_num

	pass