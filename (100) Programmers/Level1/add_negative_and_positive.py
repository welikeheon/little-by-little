'''
음양 더하기
https://programmers.co.kr/learn/courses/30/lessons/76501
'''


def solution(absolutes, signs):
    answer = 0
    for index, elem in enumerate(absolutes):
        if signs[index] == False:
            answer = answer - abs(elem)
        else:
            answer = answer + abs(elem)

    return answer
