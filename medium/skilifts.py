n = int(input())

data = []

for i in range(n):
    x, y, a = [int(x) for x in input().split()]
    data.append((x, y, a))

print(data)
