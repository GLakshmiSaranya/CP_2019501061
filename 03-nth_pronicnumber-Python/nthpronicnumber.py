# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
	count = 0
	num = 1
	
	while count < n:
		num += 1
		if isPronicNumber(num):
			count += 1
	return num

def isPronicNumber(n):
	i = 0
	sqr = int(n ** 0.5)

	while i <= sqr:
		res = i * (i + 1)
		if x == res:
			return True
		i += 1
	return False