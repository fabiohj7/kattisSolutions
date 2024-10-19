def is_harshad(x: int):
    num = str(x)
    total = 0

    for i in num:
        total += int(i)
    if x % total == 0:
        return True
    return False


n = int(input())

while not is_harshad(n):
    n += 1
print(n)
