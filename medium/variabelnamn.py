from collections import defaultdict

n = int(input())
nums = defaultdict(int)
for i in range(n):
    c = int(input())
    temp = c
    while temp in nums:
        temp = c * (nums[c] + 1)
        nums[c] += 1
    nums[temp] += 1

for i in nums:
    print(i)
