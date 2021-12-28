def solution(arr1, arr2):
    d1, d2, d3 = len(arr1), len(arr1[0]), len(arr2[0])
    
    # init the answer matrix
    answer_matrix = [[0 for x in range(d3)] for y in range(d1)]
    
    # do mult.
    for i in range(d1):
        for j in range(d3):
            for k in range(d2):
                answer_matrix[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer_matrix
    