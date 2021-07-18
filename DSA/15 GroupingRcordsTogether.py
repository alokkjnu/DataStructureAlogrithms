#grouping records together based on a field

from operator import itemgetter
from itertools import groupby

from collections import defaultdict

rows = [
    {'address':'512 N ClARK','date':'07/01/2012'},
    {'address':'5148 N ClARK','date':'07/04/2012'},
    {'address':'5800 E 58TH','date':'07/02/2012'},
    {'address':'5645 N REVENSWOOD','date':'07/03/2012'},
    {'address':'1060 W ADDISION','date':'07/02/2012'},
    {'address': '4801 N BROADWAY','date':'07/02/2012'},
    {'address':'1039 W GRANVILLE','date':'07/01/2012'},
    {'address':'2122 N CLARK','date':'07/04/2012'},
    {'address':'2254 S DC','date':'07/01/2012'},
]

#sort by the desired filed first

rows.sort(key=itemgetter('date'))

#iterate in groups
for date, items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)


rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for i in rows_by_date['07/01/2012']:
    print(i)