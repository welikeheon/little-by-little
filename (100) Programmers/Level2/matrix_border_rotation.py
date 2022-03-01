def rotate(sy, sx, ey, ex, matrix):
    min_val = 1e9
    
    # get the min val
    for y in range(sy, ey+1):
        min_val = min(min_val, matrix[y][sx], matrix[y][ex])
    for x in range(sx, ex+1):
        min_val = min(min_val, matrix[sy][x], matrix[ey][x])
    
    # left col
    tmp1 = matrix[sy][sx]
    for y in range(sy+1, ey+1):
        matrix[y-1][sx] = matrix[y][sx]
        
    # upper row
    tmp2 = matrix[sy][ex]
    min_val = min(min_val, tmp2)
    for x in range(ex-1, sx, -1):
        matrix[sy][x+1] = matrix[sy][x]
    matrix[sy][sx+1] = tmp1
    
    # right col
    tmp3 = matrix[ey][ex]
    for y in range(ey-1, sy, -1):
        matrix[y+1][ex] = matrix[y][ex]
    matrix[sy+1][ex] = tmp2
    
    # lower row
    tmp4 = matrix[ey][sx]
    for x in range(sx+1, ex):
        matrix[ey][x-1] = matrix[ey][x]
    matrix[ey][ex-1] = tmp3
    matrix[ey-1][sx] = tmp4

    return min_val
        
def solution(rows, cols, queries):
    answer = []
    matrix = [[x+1+cols*y for x in range(cols)] for y in range(rows)]
    
    for sy, sx, ey, ex in queries:
        answer.append(rotate(sy-1, sx-1, ey-1, ex-1, matrix))
    
    return answer