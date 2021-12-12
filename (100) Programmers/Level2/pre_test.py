def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answers_len = len(answers)
    
    first_stu = [first[i%5] for i in range(answers_len)]
    second_stu = [second[i%8] for i in range(answers_len)]
    third_stu = [third[i%10] for i in range(answers_len)]
    
    students = [first_stu, second_stu, third_stu]
    max_ = 0
    for i in range(3):
        cnt = 0
        for j in range(answers_len):
            if answers[j] == students[i][j]:
                cnt += 1
        if len(answer) == 0 or cnt == max_:
            answer.append(i+1)
            max_ = cnt
        elif cnt > max_:
            answer.pop()
            answer.append(i+1)
            max_ = cnt
    
    return answer



print(solution([1,3,2,4,2]))