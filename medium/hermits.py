n = int(input())
ppl = list(map(int, input().split()))
m = int(input())

noise = ppl.copy()

for _ in range(m):
    x, y = map(int, input().split())
    noise[x - 1] += ppl[y - 1]
    noise[y - 1] += ppl[x - 1]

ans = min(range(n), key=lambda i: (noise[i], i))
print(ans + 1)
