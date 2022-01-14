def to_K_nary(n, k):
    mult = 1
    result = 0
    while n > 0:
        result += mult * (n % k)
        mult *= 10
        n //= k
    return result

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(pow(n,0.5))+1):
        if n%i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    Knary = str(to_K_nary(n, k))

    # split by '0'
    splitted = Knary.split('0')
    for s in splitted:
        if s and is_prime(int(s)):
            answer += 1
    
    return answer