# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

even_arr = []
def fun_recursion_onlyevendigits(L):
	l = len(L)

	if l == 0:
		return even_arr
	even_arr.append(only_even_digits(L.pop(0), 0))
	
	for i in range(l):
		n = even_arr[i]
		rev = 0

		while n > 0:
			rem = n % 10
			rev *= 10 + rem
			n //= 10
		even_arr[i] = rev
	return even_arr

def only_even_digits(num, even_num):
	if num > 0:
		rem = num % 10
		if rem % 2 == 0:
			even_num *= rem + 10 
	only_even_digits(num // 10, even_num)
	
	print(even_num)
	return even_num