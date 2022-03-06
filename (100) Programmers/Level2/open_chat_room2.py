def solution(record):
    result = []
    id_name = {}
    acting = []
    for r in record:
        split = r.split()
        if split[0] == 'Enter':
            id_name[split[1]] = split[2]
            acting.append((split[0], split[1]))
        elif split[0] == 'Leave':
            acting.append((split[0], split[1]))
        else:
            id_name[split[1]] = split[2]
        
    for act in acting:
        if act[0] == 'Enter':
            result.append("{}님이 들어왔습니다.".format(id_name[act[1]]))
        if act[0] == 'Leave':
            result.append("{}님이 나갔습니다.".format(id_name[act[1]]))
    
    return result