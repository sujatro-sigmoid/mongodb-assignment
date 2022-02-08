# Sujatro - Sigmoid MongoDB Assignment

import pymongo
from comments.comments_functions import comments
from movies.movies_functions import movies
from theaters.theaters_functions import theaters
from users.users_functions import users

if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client["mflix"]

    print("'Comments' queries...")
    comments(db)
    print('\n')
    print("'Movies' queries...")
    movies(db)
    print('\n')
    print("'Theaters' queries...")
    theaters(db)
    print('\n')
    users(db)

    collections = db['comments']

