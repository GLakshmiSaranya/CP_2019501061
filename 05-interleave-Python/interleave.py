# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.

def fun_interleave(s1,s2):
	l1 = len(s1)
	l2 = len(s2)
	res = ''

	if l1 == l2:
		for i in range(0, l1):
			res += s1[i] + s2[i]

	elif l1 < l2:
		for i in range(0, l1):
			res += s1[i] + s2[i]
		res += s2[l1: ]
	elif l2 < l1:
		for i in range(0, l2):
			res += s1[i] + s2[i]
		res += s1[l2: ]
	
	return res