x = int(input())

nums = []
for i in range(x):
    nums.append(int(input()))

mi = min(nums)
ma = max(nums)

res = ma / 2

ans = max((mi - res), 0)
print(int(ans))
