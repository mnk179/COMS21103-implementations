import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def randomisedPartition(A, p, r):
    i = random.randrange(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomisedSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = randomisedPartition(A, p, r)
    k = q - p + 1
    if i == k: # the pivot value is the answer
        return A[q]
    elif i < k:
        return randomisedSelect(A, p, q - 1, i)
    else:
        return randomisedSelect(A, q + 1, r, i - k)
