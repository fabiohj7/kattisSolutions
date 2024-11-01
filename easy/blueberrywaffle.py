import math

r, f = [int(x) for x in input().split()]

rotation = f / r

fraction = rotation - int(rotation)

if fraction > 0.5:
    rotation = math.ceil(rotation)
else:
    rotation = math.floor(rotation)

if rotation % 2 == 0:
    print('up')
else:
    print('down')
