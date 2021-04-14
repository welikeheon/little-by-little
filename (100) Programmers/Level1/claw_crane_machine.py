'''
크레인 인형뽑기 게임 (Level 1)
https://programmers.co.kr/learn/courses/30/lessons/64061
'''

# from collections import deque


def pick(lst):
    for index, elem in enumerate(lst):
        if elem > 0:
            val = elem
            lst[index] = 0
            return (val, lst)
    return (None, lst)


def solution(board, moves):
    answer = 0
    newboard = []
    queue = []
    for y in range(len(board)):
        tmp = []
        for x in range(len(board)):
            tmp.append(board[x][y])
        newboard.append(tmp)

    moves = [i - 1 for i in moves]

    for m in moves:
        val, lst = pick(newboard[m])
        if val != None:
            queue.append(val)
        newboard[m] = lst

        if len(queue) > 1:
            for e in range(len(queue)):
                if len(queue) > 1 and queue[-1] == queue[-2]:
                    answer += 2
                    queue = queue[0:-2]
    return answer
