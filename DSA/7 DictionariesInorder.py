#Keeping Dictionaries in Order

from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key,d[key])

import json
d = json.dumps(d)
print(d)