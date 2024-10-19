l, d, x = int(input()), int(input()), int(input())
print(min(i for i in range(l, d + 1) if sum(map(int, str(i))) == x))
print(max(i for i in range(l, d + 1) if sum(map(int, str(i))) == x))
