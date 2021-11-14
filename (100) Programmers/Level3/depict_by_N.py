def solution(N, number):
    answer = 0
    s = [set() for _ in range(9)]
    
    for i in range(1, 9):
        s[i].add(int(str(N)*i))
    
    if number in s[1]:
        return 1
    
    # dynamic programming
    for i in range(2, 9):
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i
            break
    else:
        answer = -1
            
    return answer