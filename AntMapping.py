from itertools import permutations
import random

#This function takes in a list, and outputs a list that has the same maximum value for each element, but which has been affected by an additive Ant Walking map to simulate additive randomness

def remaplist(lst):
    mxval = max(lst)
    outlst = []
    for elem in lst: 
        adr = random.randrange(mxval)
        elem += adr
        if elem in outlst:
            elem += 1
        if elem <= mxval:
            outlst.append(elem)
        if elem > mxval:
            elem -= mxval
            outlst.append(elem)     
  
    return outlst

#Here is a sample list to try:
tstlst = [1, 4, 3, 6, 8, 7, 3, 45]
outlst = remaplist(tstlst)

#Here is one possible list created:
print(outlst)