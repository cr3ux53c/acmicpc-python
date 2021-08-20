# https://www.acmicpc.net/problem/10250

def sol(H, W, N, deb=False):
    import math
    return H if N % H == 0 else N % H, math.ceil(N / H)

if __name__ == "__main__":
    T = int(input())

    for test_case in range(T):
    # for test_case in ['6 12 10', '30 50 72']:
        H, W, N = map(int, input().split())
        floor, number = sol(H, W, N, True)
        print('{:d}{:02d}'.format(floor, number))
