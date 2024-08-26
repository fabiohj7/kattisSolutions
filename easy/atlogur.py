n = int(input())
knights = {}
for i in range(n):
    h, s = [int(x) for x in input().split()]
    knights[i] = [h, s]

x = 0
y = 1
while y < n and x < n:
    # Knight i attacks knight i + 1
    knights[y][0] -= knights[x][1]

    if knights[y][0] <= 0:
        y += 1

    else:
        knights[x][0] -= knights[y][1]
        if knights[x][0] <= 0:
            x = y
            y += 1

print(x + 1)
