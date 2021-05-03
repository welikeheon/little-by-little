'''
같은 숫자는 싫어!
https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3#
'''


def solution(arr):
    answer = []

    for num in range(0, len(arr) - 1):
        if arr[num] != arr[num + 1]:
            answer.append(arr[num])

    if len(answer) == 0:
        answer.append(arr[0])

    if arr[-1] != answer[len(answer) - 1]:
        answer.append(arr[-1])

    return answer
