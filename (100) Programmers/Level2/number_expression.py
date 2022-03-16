def solution(n):
    answer = 0
    for i in range(1, n+1):
        sub_total = 0
        adder = i
        while sub_total < n:
            sub_total += adder
            adder += 1
        if sub_total == n:
            answer += 1
    
    return answer