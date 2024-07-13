import sys
from collections import defaultdict

people = defaultdict(list)
tmp = input()
n, _ = [int(x) for x in tmp.split()]

for line in sys.stdin:
    line = line.split()
    if not line:
        break

    # if int(line[0]) not in people:
    #     people[int(line[0])] = [int(line[1])]
    # else:
    people[int(line[0])].append(int(line[1]))

ans = set()
for i in range(1, n + 1):
    ans.add("-".join(str(x) for x in sorted(people[i])))

print(len(ans))
