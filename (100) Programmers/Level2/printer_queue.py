from collections import deque
import heapq

def solution(priorities, location):
    answer = 0
    pri_i = deque()
    tmp_q = []
    printing_q = deque()
    
    for i, p in enumerate(priorities):
        pri_i.append((p, i))
        
    printing_q.append(pri_i[0])
    
    for i in range(1, len(pri_i)):
        if printing_q[-1][0] >= pri_i[i][0]:
            printing_q.append(pri_i[i])
        else:
            while printing_q:
                heapq.heappush(tmp_q, printing_q.popleft())
            printing_q.append(pri_i[i])
            while tmp_q[0] 

    while tmp_q:
        printing_q.append(heapq.heappop(tmp_q))
    
    print(printing_q)

    return answer

solution([2,3,9,5,1,1], 2)