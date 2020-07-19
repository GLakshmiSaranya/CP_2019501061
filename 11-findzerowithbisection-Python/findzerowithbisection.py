# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.

def findzerowithbisection(x, epsilon):
	# epsilon and step are initialized
	# don't change these values
	# epsilon
	# your code starts here
	guess = 0
	low = 0
	high = x

	while True:
		guess == (low + high) / 2
		g_sq = guess ** 2
		diff = abs((g_sq) - x)

		if diff <= epsilon:
			break
		if x >= g_sq:
			low = guess
		else:
			high = guess

	return guess