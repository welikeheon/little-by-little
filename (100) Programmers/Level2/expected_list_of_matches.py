import math

def solution(n,a,b):
    start = 1
    end = n
    answer = int(math.log2(n))
    if a > b:
        a, b = b, a
    while True:
        half = (start+end)//2
        if start <= a <= half and half < b <= end:
            break
        if half < a:
            start = half+1
        if half >= b:
            end = half
        answer -= 1
        
    return answer