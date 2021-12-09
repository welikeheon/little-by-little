def solution(board, moves):
    answer = 0
    moved = []
    stacks = []
    
    # create stacks
    for i in range(len(board[0])):
        stacks.append(list())
        for j in range(len(board)):
            if board[j][i] != 0:
                stacks[i].append(board[j][i])
        stacks[i] = stacks[i][::-1] # flip the stack
    
    for m in moves:
        if stacks[m-1]: # if there is something to be popped
            e = stacks[m-1].pop() # pop it
            
            # if the popped element is same with the top of moved stack,
            if moved and moved[-1] == e:
                moved.pop()  # pop the top of the moved stack
                answer += 2  # two elements are removed
            else:
                moved.append(e)
    
    return answer