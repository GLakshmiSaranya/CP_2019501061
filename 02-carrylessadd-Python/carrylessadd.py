# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.

def fun_carrylessadd(x, y):
	carryless_sum = 0
	pos = 1
	while x != 0 or y != 0:
		temp = ((x % 10) + (y % 10))

		if temp >= 10:
			temp %= 10
		carryless_sum += temp * pos

		pos *= 10
		x //= 10
		y //= 10
	return carryless_sum