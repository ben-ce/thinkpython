memo = {}


def new_ack(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return new_ack(m-1, 1)

    if (m, n) in memo:
        return memo[(m, n)]
    else:
        memo[m, n] = new_ack(m-1, new_ack(m, n-1))
        return memo[(m, n)]
