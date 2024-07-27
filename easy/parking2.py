t = int(input())

for _ in range(t):
    n = int(input())
    x = map(int, input().split())

    x = sorted(x)
    ans = 0
    for i in range(len(x) - 1):
        ans += abs(x[i] - x[i + 1])
    print(ans * 2)
