'''
CodeSignal > Arcade > Intro > The Journey Begin > Check Palindrome

Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
'''


def checkPalindrome(inputString):
    lst = list(inputString)
    lst_reversed = lst[::-1]

    for num in range(len(lst)):
        if lst[num] == lst_reversed[num]:
            continue
        return False
    return True
