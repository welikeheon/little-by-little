from itertools import permutations

def is_prime(s, primes):
    if not s or int(s) in primes or int(s) <= 1:
        return False
    n = int(s)
    if n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def dfs(s, numbers, idx, primes):
    global ans
    if is_prime(s, primes):
        primes.add(int(s))
    if idx >= len(numbers):
        return
    
    dfs(s+numbers[idx], numbers, idx+1, primes)
    dfs(s, numbers, idx+1, primes)
        
def solution(numbers):
    primes = set()
    nums = [n for n in numbers]
    nums_perm = list(map("".join, permutations(nums)))
    for num in nums_perm:
        dfs("", num, 0, primes)
    
    answer = len(primes)
    
    return answer