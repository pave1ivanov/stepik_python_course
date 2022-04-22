def c(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return c(n=n-1, k=k) + c(n=n-1, k=k-1)


n, k = map(int, input().split())
print(c(n, k))
