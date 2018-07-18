# S = [1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 0, 0,
#      -2, 2, -5, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12, -34, 100, 99, 1, 2, 5, 6, 7, 3, 5, 8, -33, -5, -72, 12,
#      -34, 100, 99]
S = [2, 7, 11, 15]


target = 3
import time

min = 9999
A = sorted(S)
start = time.time()
i = 0
j = len(A) - 1
for k in range(len(A)):
    while i < j:
        n = A[i] + A[j]
        if n < target-A[k] and k != i + 1:
            i += 1
        elif n > target-A[k] and k != j - 1:
            j -= 1
        else:
            break
    if abs((n + A[k]) - target) < min and k != i and k != j:
        min = abs((n + A[k]) - target)
        ret = n + A[k]
    i = 0
    j = len(A) - 1
print(ret)

# print(ret, time.time()-start)
