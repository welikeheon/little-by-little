# n 학생 수
# lost 도난당한 학생
# reverse 여벌의 옷 가지고 있는 학생(본인 것 포함 2벌.. 굉장히 수상하다....)
# 체육수업 들을 수 있는 최댓값..
def solution(n, lost, reserve):
    answer = 0
    students = [1] * n

    for i in reserve:
        students[i - 1] = 2

    for i in lost:
        # 여벌옷 가져온 사람들이 체육복을 털렸을때는...
        if students[i - 1] == 2:
            # 1벌은 남아있다고 가정...
            students[i - 1] = 1
        else:
            students[i - 1] = 0

    print(students)

    # for order in range(1, len(students)):
    #     if students[order] > 0 and students[order - 1] < 2:
    #         students[order] = students[order] - 1
    #         students[order - 1] = students[order - 1] + 1
    # 11번 빼고 다됨
    for order in range(0, len(students) - 1):
        if students[order] == 2:
            if students[order - 1] == 0 and order > 0:
                students[order] = students[order] - 1
                students[order - 1] = students[order - 1] + 1

            elif students[order + 1] == 0:
                students[order] = students[order] - 1
                students[order + 1] = students[order + 1] + 1
        print(students)

    # 1개를 shift 해봅시다....
    for order in range(0, len(students) - 1):
        if students[order] == 0:
            if students[order + 1] == 1:
                students[order] = 1
                students[order + 1] = 0

    print(students)
    # for i in range(len(students) -2, -1, -1):
    #     if students[i] == 2:
    #         if students[i + 1] == 0:
    #             students[i] = students[i] - 1
    #             students[i + 1] = students[i + 1] + 1
    #         elif students[i - 1] == 0:
    #             students[i] = students[i] - 1
    #             students[i - 1] = students[i - 1] + 1

    summary = 0
    for elem in students:
        if elem > 0:
            summary = summary + 1
    return summary
