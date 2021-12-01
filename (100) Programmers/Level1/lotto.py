def solution(lottos, win_nums):
    winning = [6,5,4,3,2,1]  # do not use the first element
    
    corrects = len(set(lottos) & set(win_nums))
    whatif = len([x for x in lottos if x == 0])
    max_ = corrects + whatif -1
    min_ = corrects -1
    
    if max_ < 0:
        max_ = 0
    if min_ < 0:
        min_ = 0
    return [winning[max_], winning[min_]]
    