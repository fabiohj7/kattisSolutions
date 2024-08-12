def to_number(num, source):
    decimal = ''
    for item in num:
        decimal += str(source.index(item))
    return decimal


def number_decimal(number: str, source):
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[-(i + 1)]) * (len(source)**i)
    return decimal


def decimal_target(decimal: int, target):
    ans = ''
    while decimal > 1:
        ans = str(decimal % len(target)) + ans
        decimal = decimal // len(target)
    return ans


def final_ans(ans, target):
    final = ''
    for item in ans:
        final += target[int(item)]
    return final


def main():
    n = int(input())
    for _ in range(n):
        num, source, target = input().split()
        number = ''
        ans = ''
        decimal = 0
        number = to_number(num, source)
        decimal = number_decimal(number, source)
        ans = decimal_target(decimal, target)
        ans = final_ans(ans, target)
        print(ans)


if __name__ == "__main__":
    main()
