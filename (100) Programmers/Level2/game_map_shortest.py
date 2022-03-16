from collections import deque

def bfs(y, x, maps):
    q = deque([(y, x)])
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    visited[y][x] = 1
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in dirs:
            ny, nx = dy+cy, dx+cx
            if not (0 <= ny < len(maps) and 0 <= nx < len(maps[0])):
                continue
            if maps[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[cy][cx]+1
                q.append((ny, nx))
    return visited[-1][-1] if visited[-1][-1] > 0 else -1

def solution(maps):
    answer = bfs(0, 0, maps)
    
    return answer
