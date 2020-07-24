# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def nthlychrelnumbers(n):
	# your code goes here
	count = 0
	num = 1

	while count < n:
		num += 1
		rev = reverse(n)
		res = n + rev

		if isPalindrome(res):
			count += 1

		num += 1
	return num
	pass

def reverse(n):
	rev = 0

	while n > 0:
		rem = n % 10
		rev = rev * 10 + rem
		n //= 10
	return rev

def isPalindrome(n):
	return n == reverse(n)