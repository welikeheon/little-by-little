def solution(board, skill):
    N = len(board)
    M = len(board[0])
    final_calc = [[0] * M for _ in range(N)]

    # prefix sum ready
    for s in skill:
        degree = s[5]

        if s[0] != 1:
            degree = -degree
        
        final_calc[s[1]][s[2]] -= degree
        if s[4] + 1 < M:
            final_calc[s[1]][s[4]+1] += degree
        if s[3] + 1 < N:
            final_calc[s[3]+1][s[2]] += degree
        if s[3] + 1 < N and s[4] +1 < M:
            final_calc[s[3]+1][s[4]+1] -= degree
        
    # down prefix sum
    for i in range(1, N):
        for j in range(M):
            final_calc[i][j] += final_calc[i-1][j]
    
    # right prefix sum
    for i in range(1, M):
        for j in range(N):
            final_calc[j][i] += final_calc[j][i-1]
    
    # final calculation
    for i in range(N):
        for j in range(M):
            board[i][j] += final_calc[i][j]

    # count the number greater than zero
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                answer += 1
    return answer
    