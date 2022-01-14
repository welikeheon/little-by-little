candidate = []
max_diff = 0

def dfs(n, ryan, apeach, i):
    '''
        n := remaining arrow
        ryan := the number of hitted arrow by ryan of each target
        apeach := the number of hitted arrow by apeach of each target
        i := array runner index
    '''
    global max_diff
    global candidate

    # base case
    # 1. if there is no extra arrow
    # 2. if the i(runner) reaches to the end and still have extra arrow
    if n == 0 or (n > 0 and i == 10):
        ryan_total = 0
        apeach_total = 0
        if i == 10: # assign the remaining arrows when i reaches the end
            ryan[10] = n

        # take a look from the point 10 ~ 1 (no need to calculate 0 points)
        for j in range(10):
            if ryan[j] > 0:
                if ryan[j] > apeach[j]:
                    ryan_total += 10-j
            if apeach[j] > 0:
                if apeach[j] >= ryan[j]:
                    apeach_total += 10-j

        diff = ryan_total - apeach_total

        # if current diff is same and is not 0,
        # which means ryan wins and the total score is same as before
        # (diff == 0 means apeach wins, so we need to discard that case)
        if diff == max_diff and diff != 0:  
            max_diff = diff
            candidate.append(ryan.copy())   # append the arry to the candidate array

        # if the current diff is larger than the max_diff,
        # which means ryan wins and the total score has changed (bigger than before)
        if diff > max_diff:     
            max_diff = diff
            candidate = [ryan.copy()]   # renew the candidate array
        return

    if n > 0 and i < 10:
        # dfs with the case that ryan has one more hitted arrow than apeach's
        ryan[i] = apeach[i]+1
        dfs(n-ryan[i], ryan.copy(), apeach, i+1)

        # dfs with the case that ryan does not hitted any arrow of the apeach's
        ryan[i] = 0
        dfs(n, ryan.copy(), apeach, i+1)

def solution(n, info):
    ryan = [0] * 11
    dfs(n, ryan.copy(), info, 0)
    
    if len(candidate) == 0:
        return [-1]
    else:   # sort by lower scores
        for c in candidate:
            c.reverse()
        candidate.sort(reverse=True)
        candidate[0].reverse()
        return candidate[0]
