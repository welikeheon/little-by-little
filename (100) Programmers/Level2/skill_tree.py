def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill)
    
    for skills in skill_trees:
        collected = []
        for s in skills:
            if s in skill_set:
                collected.append(s)
        
        collected = "".join(collected)
        if skill.find(collected) == 0:
            answer += 1
        elif not collected:
            answer += 1
    
    return answer
    