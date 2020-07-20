# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.

def fun_getaverage(s):
	arr = s.split(",")
	int_arr = []

	for i in arr:
		if i.isdigit():
			int_arr.append(i)

	l = len(int_arr)
	avg = 0.0
	if l == 0:
		return avg

	arr_sum = 0.0
	for i in int_arr:
		arr_sum += i

	avg = arr_sum / l
	return avg