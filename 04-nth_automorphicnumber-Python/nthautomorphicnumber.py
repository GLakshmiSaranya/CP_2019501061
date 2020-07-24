# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	# Your code goes here
	count = 0
	num = 1
	
	while count < n:
		num += 1
		if isAutoMorphicNumber(num):
			count += 1
	return num
	pass

def isAutoMorphicNumber(n):
	sqr = n ** 2
	
	while n > 0:
		n_rem = n % 10
		s_rem = sqr % 10

		if n_rem != s_rem:
			return False
		
		n //= 10
		sqr //= 10

	return True