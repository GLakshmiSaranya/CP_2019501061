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
	
	num = L[0]
	if num == 0:
		even_arr.append(num)
		return fun_recursion_onlyevendigits(L)
	pos = 0
	rem = 0
	while num > 0:
		t = num % 10
		if t % 2 == 0:
			rem += t * (pos ** 10)
			pos += 1
		num //= 10
	even_arr.append(rem)
	# fun_recursion_onlyevendigits(L[1:])
	return fun_recursion_onlyevendigits(L)