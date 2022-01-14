def solution(id_list, report, k):
    reported_cnt = dict()
    hist = {id_:set() for id_ in id_list}

    for r in report:
        from_usr, to_usr = r.split()
        if to_usr not in hist[from_usr]:
            hist[from_usr].add(to_usr)
            reported_cnt[to_usr] = reported_cnt.get(to_usr, 0) + 1
    
    answer = []
    for id_ in id_list:
        cnt = 0
        for reported_usr in hist[id_]:
            if reported_cnt[reported_usr] >= k:
                cnt += 1
        answer.append(cnt)
    return answer
