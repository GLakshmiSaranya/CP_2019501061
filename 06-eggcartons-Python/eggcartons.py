# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	if eggs == 0:
		return 0
	rem = eggs // 12
	if eggs / 12 > rem:
		return rem + 1
	else:
		return rem
