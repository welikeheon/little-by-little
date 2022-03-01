def solution(enroll, referral, seller, amount):
    answer = []
    its_parent = {}
    account = {}
    for i in range(len(enroll)):
        its_parent[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        child = seller[i]
        parent = its_parent[child]
        profit = 100 * amount[i]
        tribute = int(0.1 * profit)
        account[parent] = account.get(parent, 0) + tribute
        account[child] = account.get(child, 0) + profit - tribute

        # going up
        while True:
            child = parent
            profit = tribute
            if child == '-':
                break

            parent = its_parent[child]
            tribute = int(0.1 * profit)
            account[parent] = account.get(parent, 0) + tribute
            account[child] = account.get(child, 0) - tribute
    for person in enroll:
        if person in account:
            answer.append(account[person])
        else:
            answer.append(0)
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
print(solution(enroll, referral, seller, amount))
