def decimalToTernary(n):
    ternary = ''
    while n > 0:
        ternary += str(n % 3)
        n //= 3
    return ternary

def ternaryToDecimal(n):
    decimal = 0
    for i in range(len(n)):
        decimal += (3**i * int(n[-1-i]))
    return decimal

def solution(n):
    ternary = decimalToTernary(n)
    answer = ternaryToDecimal(ternary)
    
    return answer