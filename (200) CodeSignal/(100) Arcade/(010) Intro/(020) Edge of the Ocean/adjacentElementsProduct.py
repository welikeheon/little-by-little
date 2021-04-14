'''
CodeSignal > Arcade > Intro > Edge of the Ocean > Adjacent elements Product

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
'''


def adjacentElementsProduct(inputArray):
    sumlist = list()
    for num in range(len(inputArray) - 1):
        result = inputArray[num] * inputArray[num + 1]
        sumlist.append(result)
    sumlist.sort()
    return sumlist[::-1][0]
