'''
내적
https://programmers.co.kr/learn/courses/30/lessons/70128
'''


def solution(a, b):
    summary = 0
    for i, j in zip(a, b):
        summary += (i * j)
    return summary
