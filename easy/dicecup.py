n, m = [int(x) for x in input().split()]

d = {}
numbers = []
counter = 2
for i in range(1, n + 1):
    for y in range(1, m + 1):
        if i + y not in d:
            d[i + y] = 1
        d[i + y] += 1

max_values = max(d.values())
ans = [key for key, value in d.items() if value == max_values]
for item in ans:
    print(item)
