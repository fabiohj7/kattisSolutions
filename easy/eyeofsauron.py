n = input()

count1 = 0
count2 = 0
for i in n:
    if i == '|':
        count1 += 1
    elif i == '(':
        count2 = count1
        count1 = 0

if count1 == count2:
    print('correct')
else:
    print('fix')
