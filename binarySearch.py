import unittest

def binarySearch(array, target) :
	return helper(array, target, 0, len(array) - 1)

def helper(array, target, left, right) :
	while left <= right :
		mid = (left + right) // 2
		match = array[mid]
		if target == match :
			return mid
		elif target < array[mid] :
			right = mid - 1
		else :
			left = mid + 1
			
	return -1
