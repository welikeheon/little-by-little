import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort() # sort first
    
    # while there is something inside of the q
    # and the first element is lower than K
    while len(scoville) > 1 and scoville[0] < K:
        new_scoville = heapq.heappop(scoville) + \
                        2 * (heapq.heappop(scoville))
        
        # push the new element
        heapq.heappush(scoville, new_scoville)
        answer += 1
    
    # failed to make scovilles larger than K
    if scoville[0] < K:
        return -1
    
    return answer