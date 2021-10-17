def s_to_lst(s):
    q = []
    lst = []
    tmp_str = ""
    for i in range(1, len(s)-1):
        if s[i] == '{':
            q = []
        elif s[i] == '}' and (s[i+1] == '}' or s[i+1] == ','):
            q.append(int(tmp_str))
            lst.append(q)
            tmp_str = ""
        elif s[i] == ',' and (s[i+1] != '{'):
            q.append(int(tmp_str))
            tmp_str = ""
        elif s[i] == ',':
            continue;
        else:
            tmp_str += s[i]

    return lst

def solution(s):
    answer = []
    check_set = set()
    lst = s_to_lst(s)
    lst.sort(key=lambda x: len(x))
    
    for lump in lst:
        for i in range(len(lump)):
            if lump[i] in check_set:
                continue;
            answer.append(lump[i])
            check_set.add(lump[i])
    
    return answer


