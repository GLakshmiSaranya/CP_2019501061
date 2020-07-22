# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

# even_arr = []

def fun_recursion_onlyevendigits(L):
	l = len(L)
	global even_num
	even_arr = []
	
	if l == 0:
		return even_arr
		
	for i in L:
		even_num = 0
		val = only_even_digits(i)
		even_arr.append(even_rev(val))
	return even_arr

def only_even_digits(num):
	global even_num

	if num > 0:
		rem = num % 10
		print(rem)
		if rem % 2 == 0:
			even_num = rem + even_num * 10
			print("Inside", even_num)
		only_even_digits(num // 10)
	
	print("outside ", even_num)
	return even_num

def even_rev(num):
	rev = 0
	while num > 0:
		rem = num % 10
		rev = rem + rev * 10
		num //= 10
	print("rev", rev)
	return rev