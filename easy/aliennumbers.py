def to_number(num, source):
    number = []
    for item in num:
        number.append(str(source.index(item)))
    return number


def number_decimal(number: list, source):
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[-(i + 1)]) * (len(source)**i)

    return decimal


def decimal_target(decimal: int, target):
    ans = []
    if decimal == 0:
        return '0'
    while decimal >= 1:
        ans.insert(0, str(decimal % len(target)))
        decimal = decimal // len(target)
    return ans


def final_ans(ans, target):
    final = ''
    for item in ans:
        final += target[int(item)]
    return final


def main():
    n = int(input())
    for i in range(n):
        num, source, target = input().split(' ')
        number = []
        ans = []
        decimal = 0
        number = to_number(num, source)
        decimal = number_decimal(number, source)
        ans = decimal_target(decimal, target)
        ans = final_ans(ans, target)
        print(f"Case #{i + 1}: {ans}")


if __name__ == "__main__":
    main()
