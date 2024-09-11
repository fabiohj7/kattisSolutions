n, s = [int(x) for x in input().split()]
for _ in range(n):
    l, r = [int(x) for x in input().split()]
    if l <= s <= r:
        s += 1
print(s)
