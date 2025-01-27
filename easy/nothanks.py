n = int(input())
nums = [int(x) for x in input().split()]
m = max(nums)
cons = [False] * m
consecutive = set()
total = 0
for i in nums:
    cons[i - 1] = True

for t in range(m - 1):

    if cons[t] and cons[t + 1]:
        consecutive.add(t + 1)
        consecutive.add(t + 2)
        continue
    if cons[t] and t + 1 not in consecutive:
        total += t + 1

if cons[m - 1] and m not in consecutive:
    total += m
if consecutive:
    total += min(consecutive)

print(total)
