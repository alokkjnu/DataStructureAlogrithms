# Transforming and Reducing Data at the same time
import os

nums = [1,2,3,4,5]
s = sum(x * x for x in nums) 
print(s)

#Determining if any .py files exist in a directory
files = os.listdir('F:\VSPython2')
if any(name.endswith(',py') for name in files):
    print("there is python file")
else:
    print("there is no python file")

#output a tuple as csv
s = ('ACME',50,123)
print(','.join(str(x) for x in s))

#Data reduction across fields of a data structure
portfolio = [
    {'name' : 'GOOG','shares' : 50},
    {'name' : 'YHOO','shares' : 75},
    {'name' : 'AOL' , 'shares' : 20},
    {'name' : 'SCOX' , 'shares' : 65}
]
minprice = min(s['shares'] for s in portfolio)
print(minprice)
maxprice = max(s['shares'] for s in portfolio)
print(maxprice)

#Pass generator-expression as arguement
s = sum(( x * x for x in nums))
print(s)

#Pass more elegant syntax
s = sum(x * x for x in nums)
print(s)