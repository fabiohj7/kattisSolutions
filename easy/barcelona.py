_, k = [int(x) for x in input().split()]
bags = [int(x) for x in input().split()]

i = bags.index(k)

if i == 0:
    print("fyrst")
elif i == 1:
    print("naestfyrst")
else:
    print(f"{i + 1} fyrst")
