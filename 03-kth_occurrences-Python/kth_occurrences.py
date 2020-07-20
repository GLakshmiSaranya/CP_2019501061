# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.
import operator

def fun_kth_occurrences(s, n):
	dic = {}
	for i in s:
		if i in dic:
			# key = i
			# value = s.count(i)
			# print(s.count(i))
			# dic[i] = s.count(i)

			dic[i] += 1
		else:
			dic[i] = 1
		if dic[i] == n:
				return i
	
	# sorted_dict = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)

	# for i in dic:
	# 	if dic[i] == n:
	# 		print(i)
	# 		return i