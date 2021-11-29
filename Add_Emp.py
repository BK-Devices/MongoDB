from pymongo import MongoClient as mc

client = mc("mongodb://localhost:27017")
db = client["Office"]
coll1 = db["Workers"]
coll2 = db["Exworkers"]
dic = {}

try:
    id = input('Enter Employee id : ')
    print()
    if id != '':
        if coll1.find_one({'_id' : id}) or coll2.find_one({'_id' : id}):
            print('Sorry this id is already present in our collection')
        else:
            print('If you dont want to enter Age and Mobile Number put "0"')
            print('For others leave it empty\n')

            nm = input('Enter Employee Name : ')
            dp = input('Enter the Department of Employee : ')
            po = input('Enter the Post of Employee : ')
            ed = input('Enter Education of Employee : ')
            ge = input('Enter Gender of Employee : ')
            ag = int(input('Enter the Age of Employee : '))
            ct = input('Enter the City of Employee : ')
            sl = float(input('Enter Salary of Employee : '))
            mo = int(input('Enter Mobile Number without country code : '))
            em = input('Enter E-Mail id : ')

            dic['_id'] = id
            if nm != '': dic['Name'] = nm
            if dp != '': dic['Department'] = dp
            if po != '': dic['Post'] = po
            if ed != '': dic['Education'] = ed
            if ge != '': dic['gender'] = ge
            if ag > 0: dic['Age'] = str(ag)
            if ct != '': dic['City'] = ct
            if sl >= 0: dic['Salary'] = sl
            else: dic['Salary'] = 0
            if len(str(mo)) == 10: dic['Mobile'] = mo
            if em != '': dic['E-Mail'] = em

            coll1.insert_one(dic)
            print('\nEmployee is added to Workers collection\n')
    else:
        print('Wrong input')
        print('Employee is not added to Workers collection\n')

except:
    print('Wrong input')
    print('Employee is not added to Workers collection\n')