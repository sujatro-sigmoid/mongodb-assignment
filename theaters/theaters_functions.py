# 1. Top n cities with the maximum number of theaters
def city_with_max_no_theaters(collection_theaters):
    city = collection_theaters.aggregate([{"$group": {"_id": "$location.address.city", "count": {"$sum": 1}}},
                                          {"$project": {"location.address.city": 1, "count": 1}},
                                          {"$sort": {"count": -1}},
                                          {"$limit": 10}])
    for x in city:
        print(x)


# 2. top 10 theatres nearby given coordinates
def theaters_near_given_coordinates(collections, coord):
    pipeline = [
        {"$group": {"_id": {"city": "$location.address.city"}}},
        {"$match": {"location.geo.coordinates[0]": coord[0], "location.geo.coordinates[1]": coord[1]}},
        {"$limit": 10},
        {"$project": {"city_name": "$_id.city", "_id": 0}}
    ]
    nearby = collections.aggregate(pipeline)
    for x in nearby:
        print(x)

def theaters(db):
    collection_theaters = db['theaters']

    print("\n\n\n\n# 1. Top n cities with the maximum number of theaters")
    city_with_max_no_theaters(collection_theaters)

    print("\n\n\n\n# 2. top 10 theatres nearby given coordinates")
    theaters_near_given_coordinates(collection_theaters, [-93.24565, 44.85466])
