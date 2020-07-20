# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.
import operator

def fun_kth_occurrences(s, n):
	dic = {}
	freq_count = []
	S = set(s)
	
	for i in S:
		count = s.count(i)
		freq_count.append(count)

		if count in dic.keys():
			dic[count].append(i)
		else:
			dic[count] = [i]

	freq_count.sort(reverse = True)
	return dic[freq_count[n - 1]][0]