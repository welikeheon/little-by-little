from collections import Counter

def solution(food_times, k):
    answer = 0
    k += 1
    food_times_len = len(food_times)
    time_cnt = Counter(food_times).items()
    time_cnt = sorted(time_cnt)
    
    phase = 0
    runner = 0
    while k > food_times_len and runner < len(time_cnt):
        phase += 1
        k -= food_times_len
        
        # is there any same time with the phase?
        if phase == time_cnt[runner][0]:
            food_times_len -= time_cnt[runner][1]
            runner += 1
    
    # no more foods left
    if runner >= len(time_cnt):
        return -1

    runner = 0
    while k > 0 and runner < len(food_times):
        if food_times[runner] > phase:
            k -= 1
        runner += 1

    return runner