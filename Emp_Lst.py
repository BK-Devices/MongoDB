from pymongo import MongoClient as mc
import json

client = mc("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

print()
if coll.find_one():
    for doc in coll.find():
        print(json.dumps(doc, sort_keys = False, indent = 2))
        print()

else:
    print('Employees not found\n')