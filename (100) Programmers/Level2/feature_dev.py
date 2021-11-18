from collections import deque

def solution(progresses, speeds):
    answer = []
    to_be_popped = set()
    queue = deque(progresses)
    
    while queue:
        for i in range(len(queue)):
            queue[i] += speeds[i]
        
        cnt = 0
        while queue and queue[0] >= 100:
            cnt += 1
            queue.popleft()
            speeds.popleft()
        
        if cnt > 0:
            answer.append(cnt)
    
    return answer

print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]))
