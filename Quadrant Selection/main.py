# https://www.acmicpc.net/problem/14681

def sol(x, y):
    if x * y > 0:
        if x > 0:
            return 1
        else:
            return 3
    elif x > y:
        return 4
    else:
        return 2


if __name__ == '__main__':
    x = int(input()); y = int(input())
    print(sol(x, y))