# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def fun_recursions_alternatingsum(L):
	l = len(L)
	res = 0
	indx = 0

	if len(L) == 0:
		return 0
	return alternating_sum(L, res, indx)

def alternating_sum(list_L, res, indx):
	if indx == len(list_L):
		return res
	if indx % 2 == 0:
		res += list_L[indx]
		indx += 1
	else:
		res -= list_L[indx]
		indx += 1

	return alternating_sum(list_L, res, indx)