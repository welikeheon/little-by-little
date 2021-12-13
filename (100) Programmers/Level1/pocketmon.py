from collections import Counter

def solution(nums):
    hash_table = Counter(nums)
    half = len(nums) // 2

    # get the min value
    return len(hash_table) if len(hash_table) < half else half
