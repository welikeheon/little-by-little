'''
CodeSignal > Arcade > Intro > Edge of the Ocean > Almost Increasing Sequence

Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

'''


def almostIncreasingSequence(sequence):
    s = sequence
    s2 = s[:]
    deleted = 0
    if (len(s) - len(set(s))) > 1:
        return False
    elif len(set(s)) == 1:
        return True

    for i in range(len(s)-1):
        if s2[i] < s2[i+1]:
            continue
        else:
            del s[i:i+2]
            deleted += 1

    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False

    if deleted > 1:
        return False
    else:
        return True
