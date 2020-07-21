# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.

def fixmostlymagicsquare(L):
	pass
	# Your code goes here
	l = len(L)
	rows_sum = []
	cols_sum = []
	for i in L:
		rows_sum.append(sum(i))
	
	print("Row Sum elements")
	for i in rows_sum:
		print(i)

	s = 0
	for i in range(l):
		for j in range(l):
			s += L[i][j]
		cols_sum.append(s)

	print("Col Sum elements")
	for i in cols_sum:
		print(i)

	for i in rows_sum:
		if rows_sum.count(i) > 1:
			value = i
		elif rows_sum.count(i) == 1:
			pos = i

	row_index = rows_sum.index(pos)
	col_index = cols_sum.index(pos)
	change_value = pos - value

	L[row_index][col_index] -= change_value
	
	return L