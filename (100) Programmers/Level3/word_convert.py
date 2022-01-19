def diffCnt(x, y):
    cnt = 0
    for x, y in zip(x, y):
        if x != y:
            cnt += 1
    return cnt

def dfs(current, target, words):
    if current == target:
        return 1
    
    if not words:
        return 0
    
    check = []
    for w in words:
        diff = diffCnt(w, current)
        if diff == 1:
            check.append(w)
    
    min_jump = 55
    for w in check:
        loc = words.index(w)
        words.pop(loc)
        jump = dfs(w, target, words)
        
        if jump > 0 and jump < min_jump:
            min_jump = jump
    
    if min_jump == 55:
        return 0
    return min_jump + 1

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = dfs(begin, target, words)
    
    return answer

print(solution("hit", "cog", ['log', 'lot', 'dog', 'dot', 'hot', 'cog']))
