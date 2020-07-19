# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')

def fun_rotatestrings(s, n):
	res = ''
	l =len(s)

	if n == 0:
		return s
	
	if n < 0:
		n = abs(n) % l
		res = s[l - n : ] + s[ : l - n]
		return res
	n = n % l
	res = s[n : ] + s[ : n]
	return res