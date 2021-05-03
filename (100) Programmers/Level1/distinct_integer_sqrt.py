'''
정수 제곱근 판별
https://programmers.co.kr/learn/courses/30/lessons/12934
'''

from math import sqrt


def solution(n):
    answer = 0
    lst = list(map(str, str(sqrt(n))))
    ending = "".join(lst[-2:])
    print(ending)
    if ending == ".0":
        d = int(sqrt(n)) + 1
        return d ** 2
    else:
        return -1
    return answer
