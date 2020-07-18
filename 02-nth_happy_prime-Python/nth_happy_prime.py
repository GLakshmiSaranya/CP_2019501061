# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def fun_nth_happy_prime(n):
	res = 0
	count = 0
	
	while count <= n:
		res += 1
		if ishappynumber(res):
			if isPrime(res):
				count += 1
	return res

def ishappynumber(n):
	if n == 1 or n == 7:
		return True
	sum = n
	while sum > 9:
		sum = 0
		while n > 0:
			sum += (n % 10) ** 2
			n //= 10
		if sum == 1:
			return True
		n = sum
	return False

def isPrime(n):
	for i in range(2, (n // 2) + 1):
		if n % i == 0:
			return False
	return True