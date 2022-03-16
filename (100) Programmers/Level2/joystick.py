def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i, c in enumerate(name):
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
        A_runner = i + 1
        while A_runner < len(name) and name[A_runner] == 'A':
            A_runner += 1
        min_move = min([min_move, 2*i+len(name)-A_runner, i+2*(len(name)-A_runner)])
    answer += min_move
    return answer