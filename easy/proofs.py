n = int(input())
c = set()
x = 0
for i in range(n):
    x += 1
    line = input().split()
    conclusion = False
    for i in line:
        if i == '->' and not conclusion:
            conclusion = True
            continue
        if conclusion:
            c.add(i)
        else:
            if i in c:
                continue
            print(x)
            exit()
print("correct")
