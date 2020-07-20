# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	l = len(a)
	d1 = []
	d2 = []

	row_sum = 0
	col_sum = 0

	for i in range(l):
		c = 0
		for j in a:
			r = sum(j)
			c += j[i]

			if i == 0:
				row_sum = r
			elif row_sum != r:
				return False

		if i == 0:
			col_sum = c
		elif col_sum != c:
			return False

	if row_sum != col_sum:
		return False 

	i = 0
	for j in a:
		d1.append(j[i])
		d2.append(j[l - i - 1])
		i += 1
	
	d1_sum = sum(d1)
	d2_sum = sum(d2)

	if row_sum != d1_sum != d2_sum:
		return False

	return True
	pass