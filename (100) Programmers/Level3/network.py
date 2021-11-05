def solution(n, computers):
    answer = 0
    computers_set = set([_ for _ in range(1, n+1)])
    hashes = [set() for _ in range(n+1)]
    
    # create hashes
    for i in range(n-1):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                hashes[i+1].add(j+1)
                hashes[j+1].add(i+1)
    
    # DFS
    while computers_set:
        visited = set()
        stack = [computers_set.pop()] # randomly choose
        
        while stack:
            top = stack[-1]
            stack.pop()
            for computer in hashes[top]:
                if computer not in visited:
                    stack.append(computer)
                    visited.add(computer)
    
        answer += 1
        # remove computer element from computer set
        for computer in visited:
            if computer in computers_set:
                computers_set.remove(computer)
    
    return answer
    