# https://www.acmicpc.net/problem/1193

def sol(N):
    sum = 0
    for i in range(1, 9999):
        sum += i
        if sum - i + 1 <= N <= sum:
            break
    
    cnt = sum - i + 1
    if i % 2 == 0:
        return N-cnt+1, cnt+i-N
    else:
        return cnt+i-N, N-cnt+1


if __name__ == '__main__':
    ret = sol(int(input()))
    print('{}/{}'.format(ret[0], ret[1]))