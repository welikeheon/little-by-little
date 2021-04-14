'''
완주하지 못한 선수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42576
'''


def solution(participant, completion):
    answer = ''
    completion.append("z" * 20)

    for p_name, c_name in zip(sorted(participant), sorted(completion)):
        if p_name != c_name:
            return p_name

    return answer
