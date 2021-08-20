# https://www.acmicpc.net/problem/2869

def sol_legacy(A, B, V, debug=False):
    cnt_vertical = 0
    cnt_day = 0
    
    while True:
        if debug: print('cnt_vertical', cnt_vertical, '/', V)
        if cnt_vertical + A >= V:
            return cnt_day + 1
        else:
            cnt_vertical = cnt_vertical + A - B
            cnt_day += 1

def sol(A, B, V, debug=False):
    import math
    return math.ceil((V-B) / (A-B))


if __name__ == "__main__":
    
    # 1 ≤ B < A ≤ V ≤ 1,000,000,000
    test_cases = (
        [2, 1, 5],
        [5, 1, 6],
        [10, 9, 100],
        [100, 99, 1000],
        [100, 99, 1000000000],
    )

    # for A, B, V in test_cases:
    #     print(sol_legacy(A, B, V, False))
    # print()
    # for A, B, V in test_cases:
    #     print(sol(A, B, V, False))

    A, B, V = input().split()
    print(sol(int(A), int(B), int(V)))