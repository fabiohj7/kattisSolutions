x = [int(x) for x in input().split()]
ans = (x[0] * x[2] + (0.5 * x[1] * (x[2] * x[2])))
print(f'{ans:.9f}')
