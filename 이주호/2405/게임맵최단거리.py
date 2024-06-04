from collections import deque


def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(y, x):
        q = deque()
        q.append([y, x])

        while q:
            y, x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                    if maps[ny][nx] == 0:
                        continue
                    maps[ny][nx] = maps[y][x] + 1
                    q.append([nx, ny])
        return maps[len(maps) - 1][len(maps[0]) - 1]

    bfs(0, 0)

    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))