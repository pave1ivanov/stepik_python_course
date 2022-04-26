def primes():
    a = 1
    dividers = 0
    while True:
        for i in range(1, a + 1):
            if a % i == 0:
                dividers += 1
        if dividers == 2:
            yield a
        dividers = 0
        a += 1


