def solution(numbers):
    answer = ''
    numbers_extended = [((str(n)*4)[:4], str(n)) for n in numbers]
    numbers_extended.sort()
    while numbers_extended:
        answer += numbers_extended.pop()[1]
    if answer[0] == '0':
        return '0'
    return answer