from itertools import permutations
import re
def solution(expression):
    answer = -1e9
    operator_combi = list(permutations(['+', '-', '*'], 3))
    for priority in operator_combi:
        operands = list(map(int, re.split('[+*-]', expression)))
        operators = re.split('[0-9]+', expression)[1:-1]
        for p in priority:
            while p in operators:
                pvt = operators.index(p)
                operands[pvt] = eval(str(operands[pvt])+operators[pvt]+str(operands[pvt+1]))
                del operands[pvt+1]
                del operators[pvt]
        answer = max(answer, abs(int(operands[0])))
    return answer
print(solution("100-200*300-500+20"))
