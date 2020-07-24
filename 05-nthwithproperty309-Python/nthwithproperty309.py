# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	count = 0
	start_num = 309
	digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

	while count < n:
		start_num += 1
		res = start_num ** 5
		str_res = list(str(res))

		for i in digits:
			if i in str_res:
				count += 1

	return start_num

	pass