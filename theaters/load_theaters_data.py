import json
from bson import ObjectId

def theatersData(db):
    file1 = open('sample_mflix/theaters.json', 'r')
    data = []
    lines = file1.readlines()
    for line in lines:
        final_dictionary = json.loads(line)
        final_dictionary['_id'] = ObjectId(final_dictionary['_id']['$oid'])
        final_dictionary['theaterId'] = final_dictionary['theaterId']['$numberInt']
        final_dictionary['location']['geo']['coordinates'] = [final_dictionary['location']['geo']['coordinates'][0]['$numberDouble'],final_dictionary['location']['geo']['coordinates'][1]['$numberDouble']]
        data.append(final_dictionary)

    Collection = db["theaters"]
    if isinstance(data, list):
        Collection.insert_many(data)
    else:
        Collection.insert_one(data)