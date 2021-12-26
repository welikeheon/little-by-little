def solution(n):
    answer = ''
    matching = ['4', '1', '2']
    
    while n > 0:
        answer += matching[n % 3]
        if n % 3 == 0:  # 124 world does not tolerate 0
            n -= 1
        n //= 3
    
    return answer[::-1]