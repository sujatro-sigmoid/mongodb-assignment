# Sujatro - Sigmoid MongoDB Assignment

import pymongo
from comments.comments_functions import comments
from movies.movies_functions import movies
from theaters.theaters_functions import theaters

if __name__ == "__main__":
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client["mflix"]

        # print("'Comments' queries...")
        # comments(db)
        # print('\n')
        print("'Movies' queries...")
        movies(db)
        # print('\n')
        # print("'Theaters' queries...")
        # theaters(db)

    except:
        print("Unable to connect to mongodb")
