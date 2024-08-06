from collections import deque


def main():
    r, c = [int(x) for x in input().split()]
    n = r * c

    ans = 0
    for i in range(1, 1 << n):
        # for i in range(1, 1880):
        binary = f'{i:b}'.zfill(n)
        matrix = [binary[j:j + r] for j in range(0, r * c, r)]

        ones = []
        ceros = []
        for x in range(c):
            for y in range(r):
                if matrix[x][y] == '1':
                    ones.append((x, y))
                else:
                    ceros.append((x, y))

        connected = check_around(ones, matrix, r, c)
        if len(connected) == len(ones):
            hole = False
            if ceros:
                hole = check_holes(ceros, matrix, r, c)
            if not hole:
                # for item in matrix:
                #     print(f"\033[92m{item}\033[0m")
                # print("Plus 1")
                ans += 1
            else:
                # print()
                # for item in matrix:
                #     print(f"\033[91m{item}\033[0m")
                pass

    print(ans)


def check_holes(ceros, matrix, r, c):
    to_explore = []
    for items in ceros:
        x, y = items
        if 0 < x < c and 0 < y < r:
            to_explore = deque([items])
    explored = set()
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1),
                  (1, -1)]

    while to_explore:
        x, y = to_explore.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < c and 0 <= ny < r:
                if matrix[nx][ny] == '0' and (nx, ny) not in explored:
                    explored.add((nx, ny))
                    to_explore.append((nx, ny))

    # Check if touches border
    for x, y in explored:
        if x == 0 or x == c - 1 or y == 0 or y == r - 1 and not explored:
            return False

    return True


def check_around(ones, matrix, r, c):
    to_explore = deque([ones[0]])
    explored = set([ones[0]])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while to_explore:
        x, y = to_explore.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < c and 0 <= ny < r and (
                    nx, ny) not in explored and matrix[nx][ny] == '1':
                explored.add((nx, ny))
                to_explore.append((nx, ny))

    return list(explored)


if __name__ == "__main__":
    main()
