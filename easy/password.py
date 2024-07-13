n = int(input())
lines = []
ans = 0
it = 1
x = 0

while x < n:
    line = input().strip().split()
    if not line:
        break
    lines.append(float(line[1]))
    x += 1

lines.sort(reverse=True)

for i in lines:
    ans += it * i
    it += 1
print(f"{ans:.4f}")
