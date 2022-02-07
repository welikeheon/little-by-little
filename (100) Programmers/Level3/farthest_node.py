import heapq
INF = 1e9

def dijkstra(adj_mtx, start):
    '''
        basic dijkstra algorithm with PQ
    '''
    q = [(0, start)]
    distance = [INF] * len(adj_mtx)
    distance[start] = 0
    
    while q:
        dist_, curr = heapq.heappop(q)
        if distance[curr] < dist_:
            continue
        for next_dist, next_ in adj_mtx[curr]:
            cost = next_dist + distance[curr]
            if cost < distance[next_]:
                distance[next_] = cost
                heapq.heappush(q, (cost, next_))
    
    return distance

def solution(n, edge):
    answer = 0
    adj_mtx = [list() for _ in range(n+1)]
    for n1, n2 in edge:
        adj_mtx[n1].append((1, n2))
        adj_mtx[n2].append((1, n1))

    # do dijkstra and find the optimal path for every node
    distance = dijkstra(adj_mtx, 1) 
    distance.pop(0) # pop the very left one as it means nothing
    max_val = max(distance) # target longest length
    
    for d in distance:
        if max_val == d:
            answer += 1
    
    return answer
    