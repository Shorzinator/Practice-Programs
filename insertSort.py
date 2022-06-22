def insertionSort(array):
    for i in range(1, len(array)) :
        j = i
        while j > 0 and array[j] < array[j - 1] :
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array

array = [8, 5, 2, 9, 5, 6, 3]

"""
length = int(input()
array = [int(input()) for i in range(length)]
"""

print("Sorted Array:", insertionSort(array))
