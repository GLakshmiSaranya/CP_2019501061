# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math

def fun_threelines_area(a, b, c):
	S = (a + b + c) / 2
	a = S * (S - a) * (S - b) * (S - c)
	area = math.sqrt(a)
	# print(area)
	# print(int(area))
	return int(area)