#!/usr/bin/python3
import json, datetime, http.client
from pprint import pprint

now = datetime.datetime.now()
ES_INDEX = 'pokemon-' + now.strftime('%Y%m%d')
print(ES_INDEX)

data = json.load(open('json/cards/Ultra Prism.json'))
ES_TYPE = data[0]['setCode']
print(ES_TYPE)
#pprint(data)

bulk_str = ''
for obj in data:
    bulk = {
        "create":{
            "_index": ES_INDEX,
            "_type": ES_TYPE,
            "_id": obj['id']
        }
    }
    bulk_str += json.dumps(bulk) + '\n' + json.dumps(obj) + '\n'

#print(bulk_str)
conn = http.client.HTTPConnection("localhost", 9200)
conn.request("PUT", "/_bulk", bulk_str)
response = conn.getresponse()
print(response.status, response.reason)
