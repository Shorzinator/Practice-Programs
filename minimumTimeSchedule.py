def mintime(queries) :
    queries.sort()
    total = []
    temp = 0
    for i in range(1, len(queries)) :
        tba = queries[i - 1]
        temp += tba
        total.append(temp)
        
    return sum(total)
