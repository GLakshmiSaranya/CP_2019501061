# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def fun_nth_additive_prime(n):
	count = 0
	res = 2

	while n <= count:
		sum = sum_of_digits(n)
		if is_prime(n) and is_prime(sum):
			count += 1
		if count == n:
			return res
		res += 2

def sum_of_digits(n):
	sum = 0
	while n > 0:
		sum += n % 10
		n //= 10
	return sum

def is_prime(n):
	for i in range(2, (n // 2) + 1):
		if n % i == 0:
			return False
	return True