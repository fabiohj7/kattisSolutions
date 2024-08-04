from collections import deque


def main():
    r, c = [int(x) for x in input().split()]
    n = r * c

    ans = 0
    for i in range((1 << n) - 1):
        i += 1
        binary = f'{i:b}'.zfill(n)
        matrix = [binary[j:j + c] for j in range(0, r * c, c)]
        # print()
        # for item in matrix:
        #     print(item)

        ones = []
        ceros = []
        for x in range(r):
            for y in range(c):
                if matrix[x][y] == '1':
                    ones.append((x, y))
                else:
                    ceros.append((x, y))
        connected = check_around(ones, matrix, r, c)
        # print("Connected: ", connected)
        # print("Ones: ", ones)
        hole = False
        if len(connected) == len(ones):
            if ceros:
                hole = True
                hole = check_holes(ceros, matrix, r, c)
                if hole:
                    continue
            ans += 1

    print(ans)


def check_holes(ceros, matrix, r, c):
    to_explore = deque([ceros[0]])
    explored = [ceros[0]]
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1),
                  (1, -1)]
    while to_explore:
        x, y = to_explore.popleft()
        if 0 < x < r - 1 and 0 < y < c - 1:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 >= nx >= r - 1
                        or 0 >= ny >= c - 1) and matrix[nx][ny] == '0':
                    explored.append((nx, ny))
                    to_explore.append((nx, ny))
                    return False


def check_around(ones, matrix, r, c):

    to_explore = deque([ones[0]])
    explored = [ones[0]]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while to_explore:
        x, y = to_explore.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and (
                    nx, ny) not in explored and matrix[nx][ny] == '1':
                explored.append((nx, ny))
                to_explore.append((nx, ny))

    return explored


if __name__ == "__main__":
    main()
