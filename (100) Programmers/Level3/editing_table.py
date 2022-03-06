def solution(n, k, cmd):
    answer = ''
    stk = []
    status = [1]*n
    runner = k
    
    for c in cmd:
        if c[0] == 'U' or c[0] == 'D':
            jump = int(c[2:])
            d = -1 if c[0] == 'U' else 1
            while jump > 0:
                runner += d
                if status[runner] == 1:
                    jump -= 1
        
        if c[0] == 'C':
            status[runner] = 0
            stk.append(runner)
            while runner < n and status[runner] == 0:
                runner += 1
            
            if runner >= n:
                runner = stk[-1]
                while status[runner] == 0:
                    runner -= 1
                    
        if c[0] == 'Z':
            status[stk.pop()] = 1
    
    
    for i in status:
        if i == 1:
            answer += 'O'
        else:
            answer += 'X'
            
    return answer