# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of 
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character 
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is 
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either 
# parameter is not a string, but returns True if both strings are empty (why?).

def samechars(S):
	# Your code goes here
	s1 = S[0]
	s2 = S[1]
	
	if s1 == s2:
		return True
	s1 = set(s1)
	s2 = set(s2)

	if len(s1) == len(s2) and sorted(s1) == sorted(s2):
		return True
	return False
	pass