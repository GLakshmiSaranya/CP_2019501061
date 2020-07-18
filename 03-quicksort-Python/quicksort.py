"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	low = 0
	high = len(array) - 1

	if low < high:
		pivot = partition(array, low, high)
		quicksort(array, low, pivot - 1)
		quicksort(array, pivot + 1, high)
	pass

def partition(array, low, high):
	i = low - 1
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			i += 1
			temp = array[i]
			array[i] = array[j]
			array[j] = temp
	
	temp = array[i + 1]
	array[i + 1] = array[high]
	array[high] = temp

	return i + 1