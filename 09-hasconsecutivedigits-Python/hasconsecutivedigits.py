# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	num = abs(n)
	while num > 0:
		rem = num % 10
		num //= 10
		if rem == num % 10:
			return True
	return False
	pass