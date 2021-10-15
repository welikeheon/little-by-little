import math

def solution(brown, yellow):
    answer = []

    # consider the cases of yellow carpets first,
    # then figure out it is valid for the brown carpets
    for i in range(1, (int)(math.sqrt(yellow))+1):
        h = i
        if yellow % h == 0:
            w = yellow // h
            if (w+2)*2 + h*2 == brown:
                answer.append(w+2)
                answer.append(h+2)
                break


    return answer
