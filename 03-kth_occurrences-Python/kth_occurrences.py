# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.

def fun_kth_occurrences(s, n):
	dic = {}
	for i in s:
		if i not in dic:
			key = i
			value = s.count(i)
			dic[key] = value
	
	for i in dic:
		if dic[i] == value:
			return i
