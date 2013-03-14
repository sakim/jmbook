# -*- coding: UTF-8 -*-


def solve(H, W, board):
    counter = 0
    for line in board:
        for tile in line:
            if tile == '.':
                counter += 1

    if counter % 3 != 0:
        return 0

    depth = 0
    return insert(H, W, board, depth)


def insert(H, W, board, depth):
    counter = 0
    x, y = None, None
    found = False

    for _y in range(H):
        for _x in range(W):
            if board[_y][_x] == '.':
                x, y = _x, _y
                found = True
                break
        if found:
            break

    if not found:
        return 1
    else:
        if (x + 1 < W and board[y][x + 1] == '.') and (y + 1 < H and board[y + 1][x] == '.'):  # 역 ㄱ
            board[y][x] = board[y][x + 1] = board[y + 1][x] = str(depth)
            counter += insert(H, W, board, depth + 1)
            board[y][x] = board[y][x + 1] = board[y + 1][x] = '.'

        if (x + 1 < W and board[y][x + 1] == '.') and (y + 1 < H and board[y + 1][x + 1] == '.'):  # ㄱ
            board[y][x] = board[y][x + 1] = board[y + 1][x + 1] = str(depth)
            counter += insert(H, W, board, depth + 1)
            board[y][x] = board[y][x + 1] = board[y + 1][x + 1] = '.'

        if (y + 1 < H and board[y + 1][x] == '.') and (x - 1 >= 0 and board[y + 1][x - 1] == '.'):  # _|
            board[y][x] = board[y + 1][x] = board[y + 1][x - 1] = str(depth)
            counter += insert(H, W, board, depth + 1)
            board[y][x] = board[y + 1][x] = board[y + 1][x - 1] = '.'

        if (y + 1 < H and board[y + 1][x] == '.') and (x + 1 < W and board[y + 1][x + 1] == '.'):  # |_
            board[y][x] = board[y + 1][x] = board[y + 1][x + 1] = str(depth)
            counter += insert(H, W, board, depth + 1)
            board[y][x] = board[y + 1][x] = board[y + 1][x + 1] = '.'

    return counter


if __name__ == '__main__':
    C = int(raw_input())
    for _ in xrange(C):
        H, W = map(int, raw_input().split())
        board = []
        for _ in xrange(H):
            board.append(list(raw_input().strip()))

        print solve(H, W, board)