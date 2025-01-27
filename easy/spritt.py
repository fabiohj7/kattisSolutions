n, x = [int(x) for x in input().split()]
total = 0
for _ in range(n):
    i = int(input())
    total += i

print("Jebb" if total <= x else "Neibb")
