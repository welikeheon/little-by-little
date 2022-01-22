def solution(triangle):
    answer = 0
    
    dp = triangle[0]
    for i in range(1, len(triangle)):
        memo = []
        for j in range(len(triangle[i])):
            if j == 0:
                memo.append(dp[0]+triangle[i][j])
            elif j == len(triangle[i])-1:
                memo.append(dp[-1]+triangle[i][j])
            else:
                memo.append(max(dp[j-1]+triangle[i][j], dp[j]+triangle[i][j]))
        dp = memo
    
    answer = max(dp)
    return answer