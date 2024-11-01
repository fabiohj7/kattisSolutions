n = list(input())
m = list(input())

length = min(len(n), len(m))

x = ''
y = ''
for _ in range(length):
    t1 = n.pop()
    t2 = m.pop()

    if t1 > t2:
        x += t1
    elif t1 < t2:
        y += t2
    else:
        x += t1
        y += t2

while len(n) > 0 or len(m) > 0:
    if len(n) > 0:
        t1 = n.pop()
        x += t1
    if len(m) > 0:
        t2 = m.pop()
        y += t2

if x == '':
    print('YODA')
else:
    print(int(x[::-1]))
if y == '':
    print('YODA')
else:
    print(int(y[::-1]))
