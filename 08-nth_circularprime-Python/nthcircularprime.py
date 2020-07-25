# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def nthcircularprime(n):
	# Your code goes here
	count = 0
	num = 2
	
	while count < n:
		num += 1
		
		if isCircularPrime(num):
			count += 1
			
	return num
	pass

def digitcount(n):
	count = 0
	while n > 0:
		n //= 10
		count += 1
	return count

def isPrime(n):
	for i in range(2, (n // 2) + 1):
		if n % i == 0:
			return False
	return True

def isCircularPrime(n):
	dig_count = digitcount(n)

	if isPrime(n):
		str_n = str(n)

		for i in range(0, 10, 2):
			if str(i) in str_n:
				return False
		
		for i in range(dig_count):
			temp = int(str_n[i : ] + str_n[ : i])

			if not isPrime(temp):
				return False

		return True

	return False