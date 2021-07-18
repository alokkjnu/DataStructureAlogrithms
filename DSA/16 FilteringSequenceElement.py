#filtering sequence element

mylist = [1,4,5,-5,10,-7,2,3,-1]
[n for n in mylist if n>0]

[n for n in mylist if n<0]

pos= (n for n in mylist if n> 0 )
print(pos)

for x in pos:
    print(x)

values = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x =int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int,values))
print(ivals)

import math
mylist = [1,4,-5,10,-7,2,3,-1]
c = [math.sqrt(n) for n in mylist if n>0]
print(c)

clip_neg = [ n if n > 0  else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0  else 0 for n in mylist]
print(clip_pos)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N REVENSWOOD',
    '1060 W ADDISION',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]
counts = [0,3,10,4,1,7,6,1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
ls = list(compress(addresses,more5))
print(ls)