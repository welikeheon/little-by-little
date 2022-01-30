from collections import Counter

def solution(clothes):
    answer = 1
    clothes_count = Counter([k for n, k in clothes])
    
    for counts in clothes_count.values():
        answer *= (counts+1)
    
    return answer - 1