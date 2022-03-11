import sys
sys.setrecursionlimit(int(1e7))

answer = []
def other_side(y, x, grid):
    ny, nx = y, x
    if y < 0:
        ny = len(grid)-1
    elif y >= len(grid):
        ny = 0
    elif x < 0:
        nx = len(grid[0])-1
    elif x >= len(grid[0]):
        nx = 0
    return ny, nx

def dfs(y, x, to, grid, target, cnt, visited):
    d = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
    ny, nx = y + d[to][0], x + d[to][1]
    ny, nx = other_side(ny, nx, grid)
    
    if grid[ny][nx] == 'L':
        to = (to-1)%4
    if grid[ny][nx] == 'R':
        to = (to+1)%4
        
    if (ny, nx, to) == target:
        answer.append(cnt)
        return
    
    if (ny, nx, to) not in visited:
        visited.add((ny, nx, to))
        dfs(ny, nx, to, grid, target, cnt+1, visited)
        
def solution(grid):
    global answer
    visitied = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for to in range(4):
                dfs(y, x, to, grid, (y, x, to), 1, visitied)
    
    return sorted(answer)