def solution(n, times):
    min_time = 1
    max_time = max(times) * n
    answer = 0
    
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        checked_people = 0
        for t in times:
            checked_people += mid_time // t
            if checked_people >= n: # if an examiner with t time is enough,
                break
            # else we need to use every examiner to check every person
                
        if checked_people < n:  # mid_time is not sufficient to check every person
            min_time = mid_time + 1 # find out the bigger time
        else:   # mid_time was sufficient to check every person
            max_time = mid_time - 1 # find out the smaller time
            answer = mid_time   # remember the last possible time
    return answer
    