from itertools import combinations

def valid(cols, relation):
    selected = set([tuple(row[c] for c in cols) for row in relation])
    return True if len(relation) == len(selected) else False

def solution(relation):
    answer = 0
    relation_col_len = len(relation[0])
    col_sel_combis = []
    for i in range(relation_col_len):
        col_sel_combis.extend(list(combinations(range(relation_col_len), i+1)))
    dup_candidates = []
    for cols in col_sel_combis:
        if valid(cols, relation):
            dup_candidates.append(set(cols))
    answer = set()
    # print(dup_candidates)
    for i in range(len(dup_candidates)):
        adding = True
        for j in range(len(dup_candidates)):
            if i == j:
                continue
            if dup_candidates[j].issubset(dup_candidates[i]):
                adding = False
                break
        if adding:
            answer.add(tuple(dup_candidates[i]))
    return len(answer)