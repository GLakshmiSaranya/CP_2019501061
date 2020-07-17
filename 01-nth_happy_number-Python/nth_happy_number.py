# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def fun_nth_happy_number(n):
	res = 0 
	count = 0
	
	while count <= n:
		res += 1
		if (isHappyNumber(res)):
			count += 1
	return res

def ishappynumber(n):
	if n == 1:
		return True
	sum = n
	while sum > 9:
		sum = 0
		while n > 0:
			sum += (n % 10) ** 2
			n //= 10
		if sum == 1:
			return True
		else:
			n = sum
	return False