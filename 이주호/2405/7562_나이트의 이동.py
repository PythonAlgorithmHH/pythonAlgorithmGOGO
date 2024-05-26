import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 2, 2, -2, -2, -1, 1]
dy = [2, 2, -1, 1, 1, -1, -2, -2]


def bfs(a, b):
    q = deque()
    q.append([a, b])
    pan[a][b]=1
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            return pan[x][y]-1
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= x < nul and 0 <= y < nul and pan[nx][ny]==0:
                pan[nx][ny] = pan[x][y] + 1
                q.append([nx, ny])


T = int(input())
for i in range(T):
    nul = int(input())
    pan = [[0] * nul for _ in range(nul)]
    star_x, star_y = map(int,input().split())
    end_x, end_y = map(int, input().split())

    print(bfs(star_x, star_y))