# Write the function fun_isfactorish(n) that takes a value int n, 
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits 
# (so no two digits are the same), where each of the digits is a factor of the number 
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)

def fun_isfactorish(n):
	n = abs(n)
	str_n = str(n)

	if len(str_n) == 3:
		for i in str_n:
			if str_n.count(i) > 1:
				return False
			f = fun_isfactor(int(i), n)
			if f == False:
				return False
		return True
	return False

def fun_isfactor(f, n):
    if n == 0:
        return True
    if f == 0:
        return False
    if n%f == 0:
        return True
    else:
        return False