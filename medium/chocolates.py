from collections import deque


def main():
    r, c = [int(x) for x in input().split()]
    n = r * c

    ans = 0
    for i in range((1 << n) - 1):
        i += 1
        binary = f'{i:b}'.zfill(n)
        matrix = [binary[j:j + c] for j in range(0, r * c, c)]
        for item in matrix:
            print(item)

        ones = []
        for x in range(r):
            for y in range(c):
                if matrix[x][y] == '1':
                    ones.append((x, y))
        connected = check_around(ones, matrix, r, c)
        print("Connected: ", connected)
        print("Ones: ", ones)
        if len(connected) == len(ones):
            print("MATCH!")
            ans += 1

    print(ans)


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
