import sys

n, m = [int(y) for y in input().split()]

ans = ''

matrix = []
for line in sys.stdin:
    line = line.strip()
    matrix.append(line)

y = 0
x = 0
while True:
    if y < 0 or y >= n or x < 0 or x >= m:
        break

    if matrix[y][x] != '.':
        ans += matrix[y][x]

    found = False
    for i in range(x + 1, m):
        if y < len(matrix) and i < len(matrix[y]) and matrix[y][i] != '.':
            x = i
            found = True
            break
    if not found:
        for j in range(y + 1, n):
            if j < len(matrix) and x < len(matrix[j]) and matrix[j][x] != '.':
                y = j
                found = True
                break
    if not found:
        y += 1
print(ans)
