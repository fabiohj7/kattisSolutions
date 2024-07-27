while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    holes = set()
    for _ in range(m):
        r, c = map(int, input().split())
        holes.add((r, c))

    # Pre-compute available positions for each row
    available_positions = [set(range(n)) for _ in range(n)]
    for r, c in holes:
        if 0 <= r < n and 0 <= c < n:
            available_positions[r].remove(c)

    col = set()
    posDiag = set()
    negDiag = set()
    ans = [0]

    def backtrack(row):
        if row >= n:
            ans[0] += 1
            return

        for c in list(available_positions[row]):
            if c in col or (row + c) in posDiag or (row - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(row + c)
            negDiag.add(row - c)
            backtrack(row + 1)
            col.remove(c)
            posDiag.remove(row + c)
            negDiag.remove(row - c)

    backtrack(0)
    print(ans[0])
