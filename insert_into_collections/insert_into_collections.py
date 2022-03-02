import pymongo
from bson import ObjectId


def insertComments(collection_comments):
    new_comment = {
        "name": "Sujatro Majumder",
        "email": "sujatrom@sigmoidanalytics.com",
        "movie_id": ObjectId("573a1390f29313caabcd418c"),
        "text": "Good movie.",
        "date": "300141381000"}
    collection_comments.insert_one(new_comment)


def insertMovies(collection_movies):
    new_movie = {
        "plot": "Three men hammer on an anvil and pass a bottle of beer around.",
        "genres": [
            "Short"
        ],
        "runtime": {
            "$numberInt": "1"
        },
        "cast": [
            "Charles Kayser",
            "John Ott"
        ],
        "num_mflix_comments": {
            "$numberInt": "1"
        },
        "title": "Blacksmith Scene",
        "fullplot": "A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.",
        "countries": [
            "USA"
        ],
        "released": {
            "$date": {
                "$numberLong": "-2418768000000"
            }
        },
        "directors": [
            "William K.L. Dickson"
        ],
        "rated": "UNRATED",
        "awards": {
            "wins": {
                "$numberInt": "1"
            },
            "nominations": {
                "$numberInt": "0"
            },
            "text": "1 win."
        },
        "lastupdated": "2015-08-26 00:03:50.133000000",
        "year": {
            "$numberInt": "1893"
        },
        "imdb": {
            "rating": {
                "$numberDouble": "6.2"
            },
            "votes": {
                "$numberInt": "1189"
            },
            "id": {
                "$numberInt": "5"
            }
        },
        "type": "movie",
        "tomatoes": {
            "viewer": {
                "rating": {
                    "$numberInt": "3"
                },
                "numReviews": {
                    "$numberInt": "184"
                },
                "meter": {
                    "$numberInt": "32"
                }
            },
            "lastUpdated": {
                "$date": {
                    "$numberLong": "1435516449000"
                }
            }
        }
    }
    collection_movies.insert_one(new_movie)


def insertTheaters(collection_theaters):
    new_theater = {
        "theaterId": {
            "$numberInt": "9999"
        },
        "location": {
            "address": {
                "street1": "340 W Market",
                "city": "Bloomington",
                "state": "MN",
                "zipcode": "55425"
            },
            "geo": {
                "type": "Point",
                "coordinates": [
                    {
                        "$numberDouble": "-93.24565"
                    },
                    {
                        "$numberDouble": "44.85466"
                    }
                ]
            }
        }
    }

    collection_theaters.insert_one(new_theater)


def insertUsers(collection_users):
    new_user =  {"name": "Sujatro Majumder",
                "email": "sujatrom@sigmoidanalytics.com",
                "password": "$2b$12$qM.YvmiekyYYY7p7phpK3OicbRCDkN7ESwYAnG/o9YnfHC0Mhkmbi"}

    collection_users.insert_one(new_user)


if __name__ == "__main__":
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client["mflix"]

        collection_comments = db['comments']
        collection_movies = db['movies']
        collection_theaters = db['theaters']
        collection_users = db['users']

        insertComments(collection_comments)
        insertMovies(collection_movies)
        insertTheaters(collection_theaters)
        insertUsers(collection_users)

    except:
        print("Unable to connect to mongodb")
