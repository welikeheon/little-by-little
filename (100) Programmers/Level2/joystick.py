def diff(char_):
    return ord(char_)-ord('A') if ord(char_)-ord('A') < 1+ord('Z')-ord(char_) else 1+ord('Z')-ord(char_)

def solution(name):
    answer = []
    candidate = []

    # successive As
    for i in range(len(name)):
        if name[i] == 'A':
            cnt = 0
            for j in range(i, len(name)):
                if name[j] == 'A':
                    cnt += 1
                else:
                    candidate.append([i, cnt])
                    i = j
                    break

    if len(candidate) > 0:
        for i in range(len(candidate)):
            go_back = False
            tmp_total_cnt = 0
            start_point_of_A = candidate[i][0]
            end_point_of_A = candidate[i][0]+candidate[i][1]-1
            forward_cnt = (start_point_of_A-1)*2 if start_point_of_A > 0 else 0
            if len(name)-1 > forward_cnt+(len(name)-1)-end_point_of_A:
                go_back = True

            if go_back:
                for i in range(start_point_of_A):
                    tmp_total_cnt += diff(name[i])
                tmp_total_cnt += forward_cnt+1
                for i in range(len(name)-1, end_point_of_A, -1):
                    tmp_total_cnt += diff(name[i])
                    tmp_total_cnt += 0 if i+1 == end_point_of_A else 1
                tmp_total_cnt -= 1
            else:
                for i in range(len(name)):
                    tmp_total_cnt += diff(name[i])
                    tmp_total_cnt += 0 if i+1 == len(name) else 1

            answer.append(tmp_total_cnt)
    else:
        tmp_total_cnt = 0
        for i in range(len(name)):
            tmp_total_cnt += diff(name[i])
            tmp_total_cnt += 0 if i+1 == len(name) else 1
        answer.append(tmp_total_cnt)

    answer.sort()
    return answer[0]
