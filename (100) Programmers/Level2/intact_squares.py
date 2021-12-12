def euclidGCD(a, b):
    return b if a % b == 0 else euclidGCD(b, a % b)

def solution(w,h):
    return w * h - (w + h - euclidGCD(w, h))