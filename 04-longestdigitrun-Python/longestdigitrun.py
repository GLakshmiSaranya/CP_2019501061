# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def longestdigitrun(n):
	# Your code goes here
	n = abs(n)
	current_val = n % 10
	longest_digit_run = current_val
	longest_digit_count = 1

	count = 0

	while n != 0:
		rem = n % 10
		if rem == current_val:
			count += 1
		
		else:
			current_val = rem
			count = 1
		
		if longest_digit_count == count:

			if longest_digit_run < current_val:
				current_val = longest_digit_run
		
		elif count > longest_digit_count:
			longest_digit_run = current_val

		longest_digit_run = count
		n //= 10

	return longest_digit_run
	pass