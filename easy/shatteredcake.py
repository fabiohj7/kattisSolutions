w = int(input())
n = int(input())
a = 0
for i in range(n):
    wi, li = [int(x) for x in input().split()]
    a += wi * li

ans = a / w
print(f'{ans:.0f}')
