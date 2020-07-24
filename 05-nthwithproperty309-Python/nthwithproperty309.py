# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	count = 0
	start_num = 1
	
	while count <= n:
		res = start_num ** 5
		# print(res)
		str_res = str(res)
		flag = True

		for i in range(0, 10):
			if str(i) not in str_res:
				flag = False
				break
		
		if flag:
			print(res)
			count += 1
		start_num += 1
	
	return start_num - 1

	pass