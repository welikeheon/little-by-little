from collections import Counter

def solution(people, tshirts):
    answer = []
    people.sort()
    tshirts.sort()
    
    runner1 = 0
    runner2 = 0
    
    while runner1 < len(people) and runner2 < len(tshirts):
        if people[runner1] <= tshirts[runner2]:
            answer.append(people[runner1])
            runner1 += 1
            runner2 += 1
        elif people[runner1] > tshirts[runner2]:
            runner2 += 1
    
    print(answer)
    return len(answer)
