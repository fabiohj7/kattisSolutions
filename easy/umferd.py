m = int(input())
n = int(input())
empty = 0
for _ in range(n):
    s = input()

    for i in s:
        if i == ".":
            empty += 1

print(empty / (n * m))
