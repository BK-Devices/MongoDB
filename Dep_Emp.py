from pymongo import MongoClient as mc
import json

client = mc("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

dp = input('Enter Employee department : ')
print()

if coll.find_one({'Department' : dp}):
    for doc in coll.find({'Department' : dp}):
        print(json.dumps(doc, sort_keys = False, indent = 2))
        print()

else:
    print('Employee not found of this Department\n')