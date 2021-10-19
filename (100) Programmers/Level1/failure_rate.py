from collections import Counter

def solution(N, stages):
    tmp_ans = dict()
    stages_cnt = Counter(stages)
    
    divisor = len(stages)
    for i in range(1, N+1):
        if i not in stages_cnt:
            tmp_ans[i] = 0
        else:
            dividend = stages_cnt[i]
            if divisor > 0:
                tmp_ans[i] = dividend/divisor
                divisor -= dividend
            else:
                tmp_ans[i] = 0
    return sorted(tmp_ans, key = lambda x:tmp_ans[x], reverse=True)
    