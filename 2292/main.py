# https://www.acmicpc.net/problem/2292

def sol(N):
    if N == 1:
        return 1
    range_end = 1
    for i in range(1, 16666667):
        mulsix = 6 * i
        range_start = range_end + 1
        range_end = range_start + mulsix - 1
        if range_start <= N <= range_end:
            return i + 1


if __name__ == '__main__':
    N = int(input())
    print(sol(N))