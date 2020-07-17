# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	X = distance(x1, x2, y1, y2)
	Y = distance(x2, x3, y2, y3)
	Z = distance(x1, x3, y1, y3)
	
	return trianglearea(X, Y, Z)
	pass

def distance(x1, x2, y1, y2):
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2)

def trianglearea(s1, s2, s3):
	S = (s1 + s2 + s3) / 2
	area = (S * (S - s1) * (S - s2) * (S - s3)) ** 0.5
	return area