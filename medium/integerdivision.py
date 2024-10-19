n, d = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = [i // d for i in a]
freq = {}
counter = 0

for val in ans:
    if val in freq:
        counter += freq[val]
        freq[val] += 1
    else:
        freq[val] = 1

print(counter)
