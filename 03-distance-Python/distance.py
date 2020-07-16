# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.


def fun_distance(x1, y1, x2, y2):
	# your code goes here
	X = (x2 - x1) ** 2
	Y = (y2 - y1) ** 2
	dist = (X + Y) ** 0.5
	return dist