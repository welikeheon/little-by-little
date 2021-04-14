'''
CodeSignal > Arcade > Intro > Edge of the Ocean > Matrix Elements Sum 

After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
'''


def matrixElementsSum(matrix):
    summary = 0
    marked = []
    # marked에 초기화
    for mark in range(len(matrix[0])):
        marked.append(0)

    for layer in matrix:
        for position in range(len(layer)):
            if layer[position] == 0:
                marked[position] = 1
            else:
                if marked[position] == 1:
                    continue
                else:
                    print("> add", layer[position])
                    summary += layer[position]

    return summary
