

import json
from bson import ObjectId
def usersData(db):
    file1 = open('users.json', 'r')
    data = []
    lines = file1.readlines()
    for line in lines:
        final_dictionary = json.loads(line)
        final_dictionary['_id'] = ObjectId(final_dictionary['_id']['$oid'])
        data.append(final_dictionary)


    Collection = db["users"]
    if isinstance(data, list):
        Collection.insert_many(data)
    else:
        Collection.insert_one(data)