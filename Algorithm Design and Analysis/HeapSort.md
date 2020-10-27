# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Heap Sort

Heapsort is a comparison-based sorting algorithm.
Heapsort can be thought of as an improved selection
sort: like that algorithm, it divides its input into
a sorted and an unsorted region, and it iteratively
shrinks the unsorted region by extracting the largest
element and moving that to the sorted region. The 
improvement consists of the use of a heap data structure
rather than a linear-time search to find the maximum.

### Python program to implement a Heap Sort using Heapify function - 

```
# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
	  largest = i # Initialize largest as root 
	  l = 2 * i + 1	 # left = 2*i + 1 
	  r = 2 * i + 2	 # right = 2*i + 2 

	  # See if left child of root exists and is 
	  # greater than root 
	  if l < n and arr[i] < arr[l]: 
		    largest = l 

	  # See if right child of root exists and is 
	  # greater than root 
	  if r < n and arr[largest] < arr[r]: 
		    largest = r 

	  # Change root, if needed 
	  if largest != i: 
		    arr[i],arr[largest] = arr[largest],arr[i] # swap 

		# Heapify the root. 
		heapify(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr): 
	  n = len(arr) 

	  # Build a maxheap. 
	  for i in range(n//2 - 1, -1, -1): 
		    heapify(arr, n, i) 

	  # One by one extract elements 
	  for i in range(n-1, 0, -1): 
		    arr[i], arr[0] = arr[0], arr[i] # swap 
		    heapify(arr, i, 0) 

# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
	print ("%d" %arr[i]), 

```
### Visualizing Heap Sort - 

![Algorithm Visualization](https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif)

#### Here is a visualization, using an array and tree structure, for heap sort - 

![Algorithm Visualization](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)

## Complexity

| Name                  | Best            | Average             | Worst               | Memory    | Stable    | Comments  |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :-------- |
| **Heap sort**         | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | 1         | No        |           |




## References

[Wikipedia](https://en.wikipedia.org/wiki/Heapsort)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
