def add(m, n):
    if n == 0:
        return m
    else:
        return add(m, n - 1) + 1


def mult(m, n):
    if n == 1:
        return m
    else:
        return add(m, mult(m, n - 1))


def power(x, n):
    if n == 1:
        return x
    else:
        return mult(x, power(x, n - 1))
