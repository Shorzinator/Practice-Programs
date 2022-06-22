def bubbleSort(array):
    isSorted = False
    counter = 0

    while not isSorted :
        isSorted = True
        for i in range(len(array) - 1 - counter) :
            if array[i] > array[i + 1] :
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                isSorted = False
         counter += 1       
         
    return array

array = [8, 5, 2, 9, 5, 6, 3]

"""
length = int(input()
array = [int(input()) for i in range(length)]
"""

print("Sorted Array:", bubbleSort(array))
