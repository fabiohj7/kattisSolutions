n = int(input())

numbers = []
num = int()

for _ in range(n):
    num = int(input())
    numbers.append(num)

for _ in range(n - 1, -1, -1):
    print(numbers[_])
