from itertools import permutations
import random

#This function takes in a list, and outputs a list that has the same maximum value for each element, but which has been affected by an additive Dream Frog Hopping map to simulate additive randomness

def remaplist(lst):
    mxval = max(lst)
    sbval = int(mxval / 4)
    outlst = []
    for elem in lst:
        divedic = random.randrange(10)
        if divedic < 8:
            adr = random.randrange(sbval)
            elem += adr
            if elem > mxval:
                elem -= mxval
            outlst.append(elem)
        if divedic > 7:
            val = random.randrange(mxval)
            outlst.append(val)
    return outlst

#Here is a sample list to try:
tstlst = [1, 4, 3, 6, 8, 7, 3, 45]
outlst = remaplist(tstlst)

#Here is one possible list created:
print(outlst)