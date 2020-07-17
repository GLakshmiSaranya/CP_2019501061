# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

def fun_pascaltrianglevalue(row, col):
	if row < col:
		return 0
	if col == 0 or row == col:
		return 1
	
	n = factorial(row)
	d = factorial(col) * factorial(row - col)

	# value = n!/(r!(n-r)!)
	res = n // d
	return res
	
def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n - 1)