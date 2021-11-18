def solution(prices):
    answer = [0 for _ in prices]
    stk = [(prices[0], 0)]
    
    for i in range(1, len(prices)):
        if stk[-1][0] > prices[i]:
            while stk and stk[-1][0] > prices[i]:
                top = stk.pop()
                answer[top[1]] = i - top[1]
        stk.append((prices[i], i))
    
    prices_len = len(prices)
    while stk:
        top = stk.pop()
        answer[top[1]] = prices_len - top[1] - 1

    return answer

print(solution([1, 2, 3, 2, 3]))
