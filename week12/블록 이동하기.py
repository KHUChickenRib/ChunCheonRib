from collections import deque


def move(p1, p2, board):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    pos = []

    # 이동
    for dx, dy in dirs:
        new_p1 = (p1[0] + dy, p1[1] + dx)
        new_p2 = (p2[0] + dy, p2[1] + dx)
        if board[new_p1[0]][new_p1[1]] == 0 and board[new_p2[0]][new_p2[1]] == 0:
            pos.append((new_p1, new_p2))

    # 회전
    if p1[0] == p2[0]:  # 수평
        for i in [-1, 1]:
            if board[p1[0] + i][p1[1]] == 0 and board[p2[0] + i][p2[1]] == 0:
                pos.append((p1, (p1[0] + i, p1[1])))
                pos.append((p2, (p2[0] + i, p2[1])))
    else:  # 수직
        for i in [-1, 1]:
            if board[p1[0]][p1[1] + i] == 0 and board[p2[0]][p2[1] + i] == 0:
                pos.append(((p1[0], p1[1] + i), p1))
                pos.append(((p2[0], p2[1] + i), p2))

    return pos


def solution(board):
    N = len(board)

    # 테두리 생성
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    q.append([(1, 1), (1, 2), 0])
    visited = set([(1, 1), (1, 2)])

    while q:
        p1, p2, distance = q.popleft()
        if p1 == (N, N) or p2 == (N, N):
            return distance
        for pos in move(p1, p2, new_board):
            if pos not in visited:
                q.append((*pos, distance + 1))
                visited.add(pos)
