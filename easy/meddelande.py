import sys

n, m = [int(y) for y in input().split()]

ans1 = ''
ans2 = ''

matrix = []
for line in sys.stdin:
    line = line.strip()
    matrix.append(line)

y = 0
x = 0
i = 0
j = 0
while True:
    if matrix[j][i] != '.':
        ans2 += matrix[j][i]
    if matrix[y][x] != '.':
        ans1 += matrix[y][x]
    if y + 1 < n and matrix[y + 1][x] != '.':
        y += 1
    elif x + 1 < m and matrix[y][x + 1] != '.':
        x += 1
    if j + 1 < n and matrix[j + 1][i] != '.':
        j += 1
    elif i + 1 < m and matrix[j][i + 1] != '.':
        i += 1
    else:
        y += 1
        i += 1
    if y >= n or x >= m:
        break
print(ans1)
print(ans2)
