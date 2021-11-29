from pymongo import MongoClient as mc
import json

client = mc("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

id = input('Enter Employee id : ')
print()

if coll.find_one({'_id' : id}):
    ct = input('Enter new City of Employee : ')
    dp = input('Enter new Department of Employee : ')
    dic = {}
    if ct != '': dic['City'] = ct
    if ct != '': dic['Department'] = dp
    
    coll.update_one({'_id' : id}, {'$set' : dic})
    print('\nSalary of Employee is changed\n')
    print(json.dumps(coll.find_one({'_id' : id}), sort_keys = False, indent = 2))
    print()

else:
    print('Employee not found\n')