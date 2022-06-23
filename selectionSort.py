def selectionSort(array) :
    currentIdx = 0
    while currentIdx < len(array) - 1 :
        smallestIdx = currentIdx
        for j in range(smallestIdx + 1, len(array)) :
            if array[smallestIdx] > array[j] :
                smallestIdx = j
        array[smallestIdx], array[currentIdx] = array[currentIdx], array[smallestIdx]
        currentIdx += 1
    return array

array = [8, 5, 2, 9, 5, 6, 3]

"""
length = int(input())
array = [int(input()) for i in range(length)]
"""

print("Sorted Array:", selectionSort(array))
