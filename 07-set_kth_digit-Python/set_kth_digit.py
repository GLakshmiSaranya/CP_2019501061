# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	flag = False

	if n < 0:
		flag = True
		n = n * -1
	
	num = str(n)
	length = len(num)

	if k > length:
		return 0
	
	#print(num[length - k : ])
	
	if k == length:
		num = str(d) + num[length - k : ]
	else:
		num = num[:length - 1 - k] + str(d) + num[length - k : ]
	
	if flag:
		return int(num) * -1
	return int(num)
