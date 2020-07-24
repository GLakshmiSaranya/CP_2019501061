# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def ishappyprimenumber(n):
    # Your code goes here
    res = 0
    count = 0
    
    while count <= n:
        res += 1
        if ishappynumber(res) and isPrime(res):
            count += 1
            
    return res
    pass

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

def sumofsquaresofdigit(n):
	if n < 9:
		return n ** 2
	
	sqr_digits_sum = 0

	while n > 0:
		rem = n % 10
		sqr_digits_sum += rem ** 2
		sqr //= 10

	return sqr_digits_sum 