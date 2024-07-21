def solve_equation(m, ai, bi, s, i):
    return (s * ai[i] + bi[i]) % m


def main():
    m, n, s = [int(x) for x in input().split()]
    a = []
    b = []

    for i in range(n):
        x, y = [int(x) for x in input().split()]
        a.append(x)
        b.append(y)

    q = []
    q.append((s, 0))
    done = set([s])
    while q:
        state, move = q.pop(0)

        if state == 0:
            print(move)
            return

        for i in range(n):
            new = solve_equation(m, a, b, state, i)
            if new not in done:
                done.add(new)
                q.append((new, move + 1))

    print(-1)
    return


if __name__ == '__main__':
    main()
