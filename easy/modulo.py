import sys

nums = []
ans = 0
for i in sys.stdin:
    i = int(i)
    temp = i % 42

    if temp not in nums:
        ans += 1
        nums.append(temp)

print(ans)
