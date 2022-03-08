def div_loc(p):
    cnt = 0
    pvt = p[0]
    pvts = 0
    for i in range(len(p)):
        if p[i] == pvt:
            pvts += 1
        else:
            pvts -= 1
        cnt += 1
        if pvts == 0:
            break
        
    return cnt
        
def valid(p):
    stk = []
    for i in range(len(p)):
        if p[i] == '(':
            stk.append('(')
        else:
            if not stk:
                return False
            stk.pop()
    return True

def recur(p):
    to_return = ''
    if not p:
        return to_return
    div = div_loc(p)
    u, v = p[:div], p[div:]
    if valid(u):
        to_return = u
        to_return += recur(v)
    else:
        to_return = '(' + recur(v) + ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                to_return += ')'
            else:
                to_return += '('
    return to_return

def solution(p):
    answer = recur(p)
    print(answer)
solution("()))((()")