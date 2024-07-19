import sys
from collections import defaultdict

costumes = defaultdict(int)

n = int(input())

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break

    costumes[line] += 1

min = min(costumes.values())

ans = [key for key, value in costumes.items() if value == min]
ans.sort()

for x in ans:
    print(x)
