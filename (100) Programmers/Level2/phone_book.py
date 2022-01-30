def solution(phone_book):
    answer = True
    
    number_hash = set(phone_book)
    
    for number in phone_book:
        tmp_str = ''
        for i in range(len(number)):
            # use str append instead of str slicing (slicing takes longer)
            tmp_str += number[i]    
            if tmp_str != number and tmp_str in number_hash:
                return False
    
    return True

