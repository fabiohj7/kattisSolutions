date = [int(x) for x in input().split('/')]
if date[0] > 12:
    print('EU')
elif date[1] > 12:
    print('US')
else:
    print('either')
