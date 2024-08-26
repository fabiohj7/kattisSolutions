import sys

l = []
for line in sys.stdin:
    l = [int(x) for x in line.split()]
    for i in range(len(l)):
        temp = l[i]
        check = 0
        for j in range(len(l)):
            if j == i:
                continue
            check += l[j]

        if check == temp:
            print(temp)
            break
