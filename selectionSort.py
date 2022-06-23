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
