# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(L):
	l = len(L)

	even_arr = []
	if l == 0:
		return even_arr

	for i in L:
		even_arr.append(only_even_digits(i))
	
	return even_arr

def only_even_digits(num):
	even_num = 0
	if num > 0:
		rem = num % 10
		if rem % 2 == 0:
			even_num *= rem + 10
		only_even_digits(num // 10)

	while even_num > 0:
		rem = even_num % 10
		n *= rem + 10
		even_num //= 10

	return n