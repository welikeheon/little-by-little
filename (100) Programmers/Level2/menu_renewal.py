from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        combined_courses = []
        
        for order in orders:
            combined_courses.extend(list(combinations(sorted(order), c)))

        combi_cnt = Counter(combined_courses)
        if not combi_cnt:
            continue
        max_cnt = max(combi_cnt.items(), key=lambda x:x[1])
        
        for combi, cnt in combi_cnt.items():
            if max_cnt[1] == cnt and cnt > 1:
                answer.append(combi)
        answer.sort()
        result = []
        for a in answer:
            result.append("".join(a))
    
    return result