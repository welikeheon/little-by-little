'''
모의고사 (Level 1)
https://programmers.co.kr/learn/courses/30/lessons/42840
'''


def solution(answers):
    length = len(answers)

    one = [1, 2, 3, 4, 5]  # 5
    two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

    if length > 5:
        one = [1, 2, 3, 4, 5] * ((length // len(one)) + 1)
        two = [2, 1, 2, 3, 2, 4, 2, 5] * ((length // len(two)) + 1)
        three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((length // len(three)) + 1)

    answer = {1: 0, 2: 0, 3: 0}

    for index, question in enumerate(answers):
        if question == one[index]:
            answer[1] = answer[1] + 1
        if question == two[index]:
            answer[2] = answer[2] + 1
        if question == three[index]:
            answer[3] = answer[3] + 1

    maxval = max(answer.values())

    _answer = [k for k, v in answer.items() if v == maxval]
    _answer.sort()
    return _answer
