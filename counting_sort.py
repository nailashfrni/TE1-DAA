def counting_sort(A):
    n = len(A)
    B = [None] * n

    k = A[0]
    for i in range(2, n):
        if A[i] > k:
            k = A[i]
    C = [0] * (k + 1)

    for j in range(1, n):
        C[A[j]] += 1
    for i in range(k):
        C[i] += C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1