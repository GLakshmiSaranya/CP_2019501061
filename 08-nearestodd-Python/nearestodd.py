# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

def fun_nearestodd(n):
	# num = str(n).split(".")
	# int_n = int(num)
	
	# if int(num) % 2 == 1:
	# 	return int_n
	
	# nearest_odd = int(str(num))
	# if n % 10 == 0:
	# 	return int(str(num))
	# else:

	n = int(n)

	if n % 2 == 1:
		return n
	if n % 10 == 0:
		return n - 1
	return n + 1