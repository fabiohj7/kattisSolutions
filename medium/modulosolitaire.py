from collections import deque


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

    q = deque([(s, 0)])
    done = set([s])
    while q:
        state, move = q.popleft()

        for i in range(n):
            new = solve_equation(m, a, b, state, i)
            if new not in done:
                done.add(new)
                q.append((new, move + 1))
                if new == 0:
                    print(move + 1)
                    return

    print(-1)
    return


if __name__ == '__main__':
    main()
