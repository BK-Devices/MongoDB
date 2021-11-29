from pymongo import MongoClient as mc
import json

client = mc("mongodb://localhost:27017")
db = client["Office"]
coll1 = db["Workers"]
coll2 = db["Exworkers"]

id = input('Enter Employee id : ')
dic = coll1.find_one({'_id' : id})
print()

if dic:
    print(json.dumps(dic, sort_keys = False, indent = 2))
    coll2.insert_one(dic)
    coll1.delete_one({'_id' : id})
    print('\nEmployee is removed from Workers collection\n')

else:
    print('Employee not found\n')