def tln(array) :
    result = [float("-inf"), float("-inf"), float("-inf")]
    k = 0
    for i in array :
        #print("type(sum(result)):", type(sum(result)))
        if type(sum(result)) != int :
            print("i:", i)
            result.insert(k, i)
            result = result[:3]
            print("result[k]:", result[k], "\n")
            k += 1
        else :
            print("## i:", i)
            if array.index(i) == 3 :
                result.sort(reverse = True)
                print("Sorted!")
            print("result (before):", result)
            for j in range(len(result)) :
                if i > result[j] :
                    result.insert(j, i)
                    break
            print("result (after):", result, "\n")
    return result[:3]
