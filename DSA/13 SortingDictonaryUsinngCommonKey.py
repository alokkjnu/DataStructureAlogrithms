#Sorting a List of Dictionaries by a common Key

from operator import itemgetter
rows = [
    {'fname':'Brain','lname':'Jones','uid':1003},
    {'fname':'David','lname':'Beazley','uid':1002},
    {'fname':'John','lname':'Cleese','uid':1001},
    {'fname':'Big','lname':'Jones','uid':1004},
]

rows_by_fname = sorted(rows,key=itemgetter('fname'))
print(rows_by_fname)
rows_by_uid = sorted(rows,key=itemgetter('uid'))
print(rows_by_uid)

#itemgetter() function also accecpt multiple keys

row_by_lfname = sorted(rows,key=itemgetter('fname','lname'))
print(row_by_lfname)

#itemgetter replaced by lambda expression
rows_by_fname = sorted(rows,key=lambda r:r['fname'])
print(rows_by_fname)
rows_by_lname = sorted(rows,key=lambda r:r['lname'])
print(rows_by_lname)
rows_by_lfname = sorted(rows,key=lambda r:(r['fname'],r['lname']))
print(rows_by_lfname)

print(min(rows,key=itemgetter('uid')))
print(max(rows,key=itemgetter('uid')))