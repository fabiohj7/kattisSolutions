t, n = [int(x) for x in input().split()]

times = input().split()
times = [int(x) for x in times]
times.sort()
total = 0
for x in times:
    if x + total > t * 60:
        break
    total += x
print(total)
