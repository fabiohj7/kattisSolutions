while True:
    n = int(input())

    if n == -1:
        break

    time = 0
    ans = 0
    for _ in range(n):
        s, t = [int(x) for x in input().split()]
        temp = t
        t = t - time
        time = temp
        ans += s * t
    print(f"{ans} miles")
