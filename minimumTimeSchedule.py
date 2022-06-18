def mintime(queries) :
    queries.sort()
    total = []
    temp = 0
    for i in range(1, len(queries)) :
        tba = queries[i - 1]
        temp += tba
        total.append(temp)
        
    return sum(total)

numProcesses = int(input())
queries = [int(input()) for i in range(numProcesses)]
print(mintime(queries))
