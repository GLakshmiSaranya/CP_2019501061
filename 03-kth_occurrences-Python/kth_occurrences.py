# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.
import operator

def fun_kth_occurrences(s, n):
	dic = {}
	for i in s:
		if i not in dic:
			# key = i
			# value = s.count(i)
			# print(s.count(i))
			dic[i] = s.count(i)
	
	sorted_dic = dict(sorted(dic.items(), key = operator.itemgetter(1), reverse = True))

	print(sorted_dic[n])
	return sorted_dic[n]