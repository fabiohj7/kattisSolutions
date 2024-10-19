n, k = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]

for i in range(k - 1, n, k):
    print(x[i], end=' ')
print()
