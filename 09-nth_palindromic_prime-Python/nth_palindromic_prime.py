# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

def fun_nth_palindromic_prime(n):
	count = -1
	res = 2

	while count <= n:
		if is_palindrome(res) and is_prime(res):
			count += 1

		if count == n:
			return res
		res += 1

def is_palindrome(n):
	str_n = str(n)
	if str_n == str_n[ : : -1]:
		return True
	return False

def is_prime(n):
	if n == 1:
		return False
	for i in range(2, (n // 2) + 1):
		if n % i == 0:
			return False
	return True