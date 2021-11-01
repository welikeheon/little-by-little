def solution(numbers, k):
    # stack with integers to be removed from numbers string
    stack = []
    
    # to be returned string size
    return_size = len(numbers) - k
    
    # going for the each number from numbers string -- O(n)
    for num in numbers:
        
        # something inside of stack, and 
        # there are still numbers to be removed
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        # push the new num
        stack.append(num)
    
    return "".join(stack)[:return_size]