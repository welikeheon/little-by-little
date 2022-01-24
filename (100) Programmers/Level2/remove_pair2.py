def solution(s):
    cnt = 0    
    stk1 = list(s)[::-1]
    stk2 = []
        
    while stk1:
        while stk1 and stk2 and stk1[-1] == stk2[-1]:
            stk1.pop()
            stk2.pop()
            cnt += 1
        if stk1:
            stk2.append(stk1.pop())
    
    # use float division to normalize the result
    # i.e. what if the length of the s is odd? -> should be always False
    return 1 if cnt == len(s)/2 else 0
