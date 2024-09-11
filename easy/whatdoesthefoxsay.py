import sys

n = int(input())
for _ in range(n):
    list1 = input().split()
    removal_set = set()

    for line in sys.stdin:
        l1 = line.split()
        if l1[0] == 'what':
            break
        removal_set.add(l1[2])

    ans = " ".join(x for x in list1 if x not in removal_set)
    print(ans)
