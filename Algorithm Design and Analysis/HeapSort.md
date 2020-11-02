#### Algorithms Design and Analysis - Open Ended Assignment
#### Shourya Maheshwari - A2305218495 (5CSE8X)
---
![leaves](https://user-images.githubusercontent.com/62899599/97261107-2d319900-1844-11eb-8750-4eb107f3f314.jpg)

# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Heap Sort*

Heapsort is a comparison-based sorting algorithm.
Heapsort can be thought of as an improved selection
sort: like that algorithm, it divides its input into
a sorted and an unsorted region, and it iteratively
shrinks the unsorted region by extracting the largest
element and moving that to the sorted region. The 
improvement consists of the use of a heap data structure
rather than a linear-time search to find the maximum.

### What is Binary Heap?
Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node is greater(or smaller) than the values in its two children nodes. The former is called as max heap and the latter is called min-heap. The heap can be represented by a binary tree or array.

### Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as an array and the array-based representation is space-efficient. If the parent node is stored at index I, the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

## Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree.
3. Repeat step 2 while size of heap is greater than 1.

---

### Python program to implement a Heap Sort using Heapify function - 

```
# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
# heapify
def heapify(arr, n, i):
        largest = i  # largest value
        l = 2 * i + 1  # left
        r = 2 * i + 2  # right
        # if left child exists
        if l < n and arr[ i ] < arr[ l ]:
                largest = l
        # if right child exits
        if r < n and arr[ largest ] < arr[ r ]:
                largest = r
        # root
        if largest != i:
                arr[ i ], arr[ largest ] = arr[ largest ], arr[ i ]  # swap
                # root.
                heapify(arr, n, largest)


# sort
def heapSort(arr):
        n = len(arr)
        # maxheap
        for i in range(n, -1, -1):
                heapify(arr, n, i)
        # element extraction
        for i in range(n - 1, 0, -1):
                arr[ i ], arr[ 0 ] = arr[ 0 ], arr[ i ]  # swap
                heapify(arr, i, 0)


# main
arr = [ 2, 5, 3, 8, 6, 5, 4, 7 ]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
        print(arr[ i ], end = " ")

```
![Heap_arrays](https://user-images.githubusercontent.com/62899599/97261649-438c2480-1845-11eb-982d-c31c8e07857a.jpg)

### Visualizing Heap Sort - 

![Algorithm Visualization](https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif)

#### Here is a visualization, using an array and tree structure, for heap sort - 

![Algorithm Visualization](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)
<br/>
## Complexity

Heap Sort has O(nlog n) time complexities for all the cases ( best case, average case, and worst case).

Let us understand the reason why. The height of a complete binary tree containing n elements is log n

As we have seen earlier, to fully heapify an element whose subtrees are already max-heaps, we need to keep comparing the element with its left and right children and pushing it downwards until it reaches a point where both its children are smaller than it.

In the worst case scenario, we will need to move an element from the root to the leaf node making a multiple of log(n) comparisons and swaps.

During the build_max_heap stage, we do that for n/2 elements so the worst case complexity of the build_heap step is n/2*log n ~ nlog n.

During the sorting step, we exchange the root element with the last element and heapify the root element. For each element, this again takes log n worst time because we might have to bring the element all the way from the root to the leaf. Since we repeat this n times, the heap_sort step is also nlog n.

Also since the build_max_heap and heap_sort steps are executed one after another, the algorithmic complexity is not multiplied and it remains in the order of nlog n.

Also it performs sorting in O(1) space complexity. Compared with Quick Sort, it has a better worst case ( O(nlog n) ). Quick Sort has complexity O(n^2) for worst case. But in other cases, Quick Sort is fast. Introsort is an alternative to heapsort that combines quicksort and heapsort to retain advantages of both: worst case speed of heapsort and average speed of quicksort.

| Name                  | Best            | Average             | Worst               | Memory    | Stable    |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------  |
| **Heap sort**         | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | 1         | No        |          

---

### Output of the program given above - 
![Screenshot (13)](https://user-images.githubusercontent.com/62899599/97264619-4d188b00-184b-11eb-98f7-8da806f7a802.png)

<br/>


