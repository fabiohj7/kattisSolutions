n = int(input())

counter = 0
for i in range(n):
    x = int(input())
    if x % 2 == 1:
        counter += 1

print(counter)
