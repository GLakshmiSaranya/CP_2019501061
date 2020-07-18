# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.

def isrotated(str1, str2):
	#Your code goes here
	temp = str1[0]

	if (temp not in str2):
		return False

	count = 0
	for i in str2:
		if temp == i:
			s = str2[temp: ] + str2[ :temp]
			if s == str1:
				return True
		count += 1
	return False
	pass