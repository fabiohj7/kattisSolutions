import re
import sys

operators = ['*', '/', '+', '-']
stack = []


def main():
    for line in sys.stdin:
        line = line.strip('\n')
        line = line.replace(' ', '')
        nums = re.split(r'[\+\-\*\/]', line)
        ops = re.findall(r'[\+\-\*\/]', line)
        i = 0
        ans = 0
        x = []
        while True:
            if i % 2 == 0:
                if ')' in nums[0]:
                    stack.append(nums.pop(0))
                    while True:
                        x.append(stack.pop(-1))
                        if ')' in x[-1]:
                            x[-1] = x[-1].replace(')', '')
                        if '(' in x[-1]:
                            x[-1] = x[-1].replace('(', '')
                            solve(x)
                            break
                    x.reverse()
                stack.append(nums.pop(0))

            elif i % 2 == 1:
                stack.append(ops.pop(0))
            print("Stack: ", stack)
            i += 1


def solve(l: list):
    res = 0
    temp = 0
    l = [
        int(x) if x.isdigit() or (x.startswith('-') and x[1:].isdigit()) else x
        for x in l
    ]
    for i in range(len(l) - 1):
        print(l)
        if l[i] == '+':
            res = temp + l[i + 1]
        if l[i] == '-':
            res = temp - l[i + 1]
        if l[i] == '/':
            res = temp / l[i + 1]
        if l[i] == '*':
            res = temp * l[i + 1]
        temp = l[i]

    print(res)
    return (res)


if __name__ == "__main__":
    main()
