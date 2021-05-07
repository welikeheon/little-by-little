'''
오픈채팅방
https://programmers.co.kr/learn/courses/30/lessons/42888
'''


def solution(record):
    answer = []
    userlist = dict()

    for Type, UID, *Nickname in ((s.split() for s in record)):
        if Type != "Leave":
            userlist[UID] = {"Type": Type}
            userlist[UID]["Nickname"] = Nickname

    for Type, UID, *Nickname in ((s.split() for s in record)):
        nickname = userlist[UID]["Nickname"]
        if Type == "Enter":
            answer.append(f'{nickname[0]}님이 들어왔습니다.')
        if Type == "Leave":
            answer.append(f'{nickname[0]}님이 나갔습니다.')

    return answer
