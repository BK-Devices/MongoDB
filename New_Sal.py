from pymongo import MongoClient as mc
import json

client = mc("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

id = input('Enter Employee id : ')
print()

if coll.find_one({'_id' : id}):
    try:
        sl = float(input('Enter new salary of Employee : '))
        coll.update_one({'_id' : id}, {'$set': {'Salary': sl}})
        print('\nSalary of Employee is changed\n')
        print(json.dumps(coll.find_one({'_id' : id}), sort_keys = False, indent = 2))
        print()
    except:
        print('Wrong input\n')

else:
    print('Employee not found\n')