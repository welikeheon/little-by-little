import heapq

def solution(tickets):
    answer = []
    hubs = {}
    
    for ticket in tickets:
        if ticket[0] not in hubs:
            hubs[ticket[0]] = list()
        heapq.heappush(hubs[ticket[0]], ticket[1])

    stk = ['ICN']   # visit ICN first
    path = []
    
    while stk:
        top = stk[-1]
        if top not in hubs:  # if there is nothing left hubs for the top hub
            path.append(stk.pop())
        else:   # if there is something left to visit for the top hub
            be_pushed = heapq.heappop(hubs[top])
            stk.append(be_pushed)
            if not hubs[top]:
                hubs.pop(top)

    return path[::-1]   # reverse
    
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
