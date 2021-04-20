'''
k번째 수
https://programmers.co.kr/learn/courses/30/lessons/42748
'''

# 언젠가 시도한 것..


def solution(array, commands):
    answer = []
    for elem in commands:
        start = elem[0]
        end = elem[1]
        index = elem[2]

        print(start, end, index)
        arr = array[start - 1:end]
        arr.sort()

        result = arr[index - 1]
        answer.append(result)
    return answer

# 2021. 4. 21 시도한 것..


def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[command[0] - 1:command[1]]
        arr.sort()
        answer.append(arr[command[2] - 1])
    return answer
