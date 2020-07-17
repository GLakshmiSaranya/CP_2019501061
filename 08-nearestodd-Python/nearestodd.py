# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

def fun_nearestodd(n):
	num = str(n).split(".")
	int_n = int(num[0])
	# print(int_n)
	dec_n = int(num[1])
	# print(dec_n)
	
	if int_n % 2 == 1:
		return int_n
	
	if dec_n % 10 == 0:
		return int_n - 1
	
	return int_n + 1