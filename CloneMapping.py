from itertools import permutations
import random

#This function takes in a list, and outputs a list that has the same maximum value for each element, but which has been affected by an additive RNA-cloning map to simulate additive randomness

def remaplist(lst):
    rnalst = []
    l4 = lst.pop()
    l3 = lst.pop()
    l2 = lst.pop()
    l1 = lst.pop()
    rnalst.append(l1)
    lst.append(l1)
    rnalst.append(l2)
    lst.append(l2)
    rnalst.append(l3)
    lst.append(l3)
    rnalst.append(l4)
    lst.append(l4)
    rnatot = list(permutations(rnalst, 4))
    x = len(lst)
    y = (x // 4) + 1
    outlst = []
    for z in range(y):
        ctr = random.randrange(24)
        addlst = rnatot[ctr]
        outlst.append(addlst)
    finlst = []
    for elem in outlst:
        for elem2 in elem:
            if len(finlst) <= x:
                finlst.append(elem2)
    fonlst = []
    for a in range(x):
        val = (lst[a] + finlst[a])
        if val >= (max(lst)-1):
            val -= max(lst)
        if val in fonlst:
            val += 1
        fonlst.append(val)
    return fonlst

#Here is a sample list to try:
tstlst = [1, 4, 3, 6, 8, 7, 3, 45]
outlst = remaplist(tstlst)

#Here is one possible list created:
print(outlst)