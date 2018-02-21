#!/usr/bin/python3
import json, datetime, http.client
from pprint import pprint
#num = "003"
#print(str(int(num)))
obj = {}
for i in range(1,807):
    num = format(i, '03')
    oo = {}
    oo['name'] = ''
    oo['name_zh'] = ''
    obj[str(num)] = oo

#print(json.dumps(obj))
with open('tt.json', 'w') as outfile:
    json.dump(obj, outfile, sort_keys=True)
