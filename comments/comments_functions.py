from bson import ObjectId
from datetime import datetime
from comments.load_comments_data import commentsData

def insert(collections, name, email, movie_id, text, date):
    collections.insert_one({"name":name,"email":email,"movie_id": ObjectId(movie_id),"text":text,"date":date})
    print("inserted")


def commentsTop10Users(collections):
    dictionary={}
    for row in collections.find():
        email = row['email']
        if dictionary.get(email):
            dictionary[email]+=1
        else:
            dictionary[email]=1
    users = sorted(dictionary.items(), key=lambda x: x[1],reverse=True)
    return users[:10]


def commentsTop10Movies(collections,db):
    dictionary = {}
    for row in collections.find():
        movie_id = row['movie_id']
        if dictionary.get(movie_id):
            dictionary[movie_id] += 1
        else:
            dictionary[movie_id] = 1
    a = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    data = []
    count = 0
    for k,v in a.items():
        x = db['movies'].find_one({"_id":ObjectId(k)})
        data.append(x['title'])
        count += 1
        if count == 10:
            break
    return data


def yearWiseCommentCount(collections,given_year):
    dictionary = {"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,"11":0,"12":0}
    for i in collections.find():
        x = str(i['date'])
        yr = x[0:4]
        mo = x[5:7]
        if yr is given_year:
            dictionary[mo] += 1
    return dictionary

def comments(db):

    collections = db['comments']
    # insert(collections,name ="Hello Coders" , email="sujatrom@sigmoidanalytics.com", movie_id="24322sfdsjkf3", text="Good Movie", date="12342531212313")

    top_users = commentsTop10Users(collections)
    print("Top 10 users with maximum comments:")
    print(top_users)

    top_movies = commentsTop10Movies(collections, db)
    print("Top 10 movies with maximum comments:")
    print(top_movies)

    comments_with_given_year = yearWiseCommentCount(collections, "2010")
    print("No of comments created each month in 2010:")
    print(comments_with_given_year)