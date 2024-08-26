n = int(input())

di = {}
for i in range(n):
    name, rate = input().split()
    rate = int(rate)
    di[name] = rate

di = sorted((v, k) for k, v in di.items())

print(di[-1][1])
