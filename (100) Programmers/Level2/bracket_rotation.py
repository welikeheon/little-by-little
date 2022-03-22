from collections import deque

def valid(q):
    left_bracket_type = {'{':0, '[':1,  '(':2}
    right_bracket_type = {'}':0, ']':1, ')':2}
    stk = []
    for b in q:
        if b in left_bracket_type:
            stk.append(b)
        else:
            if not stk:
                return False
            if left_bracket_type[stk[-1]] == right_bracket_type[b]:
                stk.pop()
    if stk:
        return False
    return True

def solution(s):
    answer = 0
    sq = deque(s)
    for x in range(len(s)):
        if valid(sq):
            answer += 1
        sq.append(sq.popleft())
            
    return answer