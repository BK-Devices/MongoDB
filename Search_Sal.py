from pymongo import MongoClient as mc
import json

client = mc("mongodb://localhost:27017")
db = client["Office"]
coll = db["Workers"]

try:
    sl = float(input('Enter the Salary : '))
    print()

    if coll.find_one({'Salary' : {'$gt' : sl}}):
        for doc in coll.find({'Salary' : {'$gt' : sl}}):
            print(json.dumps(doc, sort_keys = False, indent = 2))
            print()

    else:
        print('Employees not found for salary greater than %.1f\n' %sl)
except:
    print('Wrong input\n')