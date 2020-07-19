# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	str_x = str(x)
	str_y = str(y)

	len_x = len(str_x)
	len_y = len(str_y)

	if len_x != len_y:
		return False

	for i in range(0, len_x):
		if str_x[i: ] + str_x[ :i] == str_y:
			return True
		temp = len1 - i
		if str_x[temp : ] + str_x[ : temp] == str_y:
			return True
	return False
	pass