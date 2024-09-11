import sys

list1 = []
data = {}
for line in sys.stdin:
    list1 = line.split()

    if list1[0] == 'define':
        com, i, x = list1
        i = int(i)
        data[x] = i
    elif list1[0] == 'eval':
        com, a, comp, b = list1
        if a not in data or b not in data:
            print("undefined")
            continue
        if comp == '>':
            if data[a] > data[b]:
                print('true')
            else:
                print('false')
        elif comp == '<':
            if data[a] < data[b]:
                print('true')
            else:
                print('false')
        elif comp == '=':
            if data[a] == data[b]:
                print('true')
            else:
                print('false')
