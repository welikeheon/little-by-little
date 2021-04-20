'''
예산: 시간초과
https://programmers.co.kr/learn/courses/30/lessons/12982
'''

# 1차 시도
from itertools import combinations


def solution(d, budget):
    d = d[::-1]
    max_val = len(d)
    for i in range(max_val, 0, -1):
        for c in combinations(d, i):
            print(c, sum(c))
            if sum(c) == budget:
                return i

    answer = 0
    return answer
