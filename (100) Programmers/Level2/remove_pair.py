def solution(string):
    answer = 1
    stk = []
    
    for s in string:
        if not stk or stk[-1] != s:
            stk.append(s)
        elif stk[-1] == s:
            stk.pop()
    if stk:
        answer = 0

    return answer
