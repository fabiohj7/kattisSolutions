n = int(input())
for i in range(n):
    b, p = [float(x) for x in input().split()]
    bpm = (60 * b) / p
    res = 60 / p
    print(f"{bpm - res:.4f} {bpm:.4f} {bpm + res:.4f}")
