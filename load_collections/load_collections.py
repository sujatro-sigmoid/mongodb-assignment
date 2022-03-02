import pymongo
from bson import ObjectId
import json

def load_comments(db):
    collection_name = db['comments']
    collection_data = []
    f = open('../sample_mflix/comments.json', 'r')
    lines = f.readlines()
    for line in lines:
        comment = json.loads(line)
        comment['_id'] = ObjectId(comment['_id']['$oid'])
        comment['movie_id'] = ObjectId(comment['movie_id']['$oid'])
        comment['date'] = comment['date']['$date']['$numberLong']
        collection_data.append(comment)
    if isinstance(collection_data, list):
        collection_name.insert_many(collection_data)
    else:
        collection_name.insert_one(collection_data)


def load_movies(db):
    collection_name = db['movies']
    collection_data = []
    with open('../sample_mflix/movies.json') as f:
        for i in f:
            if i:
                data = json.loads(i)
                data["_id"] = ObjectId(data["_id"]["$oid"])
                collection_data.append(data)
    collection_name.insert_many(collection_data)

def load_theaters(db):
    collection_name = db['theaters']
    collection_data = []
    with open('../sample_mflix/theaters.json') as f:
        for i in f:
            if i:
                data = json.loads(i)
                data["_id"] = ObjectId(data["_id"]["$oid"])
                collection_data.append(data)
    collection_name.insert_many(collection_data)

def load_sessions(db):
    collection_name = db['sessions']
    collection_data = []
    with open('../sample_mflix/sessions.json') as f:
        for json_obj in f:
            data = json.loads(json_obj)
            data["_id"] = ObjectId(data["_id"]["$oid"])
            collection_data.append(data)
    collection_name.insert_many(collection_data)

def load_users(db):
    collection_name = db['users']
    collection_data = []
    with open('../sample_mflix/users.json') as f:
        for i in f:
            if i:
                data = json.loads(i)
                data["_id"] = ObjectId(data["_id"]["$oid"])
                collection_data.append(data)
    collection_name.insert_many(collection_data)


if __name__ == "__main__":
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client["mflix"]

        load_comments(db)
        load_movies(db)
        load_theaters(db)
        load_sessions(db)
        load_users(db)
        print("Collections loaded to mongodb")

    except:
        print("Unable to connect to mongodb")