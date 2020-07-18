# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().

def fun_replace(s1, s2, s3):
	l1 = len(s1)
	l2 = len(s2)
	s = ''

	i = 0
	while i < l1:
		if (s2 == s1 [i: i + l2]):
			s += s3
			i += l2
		else:
			s += s1[i]
			i += 1
	return s