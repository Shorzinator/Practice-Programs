def getNthFib(n):
    f0, f1, fNext = 0, 1, 0
    if n == 1 :
        return 0
    elif n == 2 :
        return 1
    else :
        for i in range(2, n) :
            fNext = f0 + f1
            f0 = f1
            f1 = fNext

    return fNext
