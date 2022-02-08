import json
from bson import ObjectId


def commentsData(db):
    file1 = open('sample_mflix/comments.json', 'r')
    data = []
    lines = file1.readlines()
    for line in lines:
        dictionary = json.loads(line)
        dictionary['_id'] = ObjectId(dictionary['_id']['$oid'])
        dictionary['movie_id'] = ObjectId(dictionary['movie_id']['$oid'])
        dictionary['date'] = dictionary['date']['$date']['$numberLong']
        data.append(dictionary)

    Collection = db["comments"] # name->comments
    if isinstance(data, list):
        Collection.insert_many(data)
    else:
        Collection.insert_one(data)
