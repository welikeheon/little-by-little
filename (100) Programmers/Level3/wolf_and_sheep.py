import copy

max_sheep = 0
def dfs(info, adj_mtx, current, avail, visited, sheep_cnt, wolf_cnt):
    global max_sheep
    sheep_cnt += (1 ^ info[current])
    wolf_cnt += info[current]
    
    # if wolves can eat whole sheeps or dfs already passed the node
    if sheep_cnt <= wolf_cnt or current in visited: # this will reduce the work
        return

    visited.add(current)    # visited status when it comes to this current node
    max_sheep = max(max_sheep, sheep_cnt)   # answer update
    avail += [adj for adj in adj_mtx[current]]  # where dfs should explore
    for next_node in avail:
        dfs(info, adj_mtx, next_node, copy.deepcopy(avail), visited.copy(), sheep_cnt, wolf_cnt)
    

def solution(info, edges):
    answer = 0
    adj_mtx = [list() for _ in range(len(info))]
    for p, c in edges:
        adj_mtx[p].append(c)
    
    avail = []
    visited = set()
    dfs(info, adj_mtx, 0, avail, visited, 0, 0)
    
    return max_sheep