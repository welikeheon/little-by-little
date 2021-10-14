import math

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    runner1 = 0
    runner2 = len(people)-1

    while runner1 < runner2:
        # remove front and back if can
        if people[runner1]+people[runner2] <= limit:
            runner2 -= 1
        runner1 += 1
        answer += 1

    answer += math.ceil(runner2-runner1+1)
    return answer
    
