import json
from bson import ObjectId


def moviesData(db):
    file1 = open('sample_mflix/movies.json', 'r')
    data = []
    lines = file1.readlines()
    for line in lines:
        dictionary = json.loads(line)
        if dictionary.get('_id'):
            dictionary['_id'] = ObjectId(dictionary['_id']['$oid'])
            if dictionary.get('year'):
                x = dictionary['year']
                if type(x) != str:
                    dictionary['year'] = dictionary['year']['$numberInt']

            if dictionary.get('runtime'):
                dictionary['runtime'] = dictionary['runtime']['$numberInt']

            if dictionary.get('released'):
                dictionary['released'] = dictionary['released']['$date']['$numberLong']

            x = dictionary['imdb']['rating']
            if type(x) != str and dictionary['imdb']['rating'].get('$numberDouble'):
                dictionary['imdb']['rating'] = dictionary['imdb']['rating']['$numberDouble']
            elif type(x) != str:
                dictionary['imdb']['rating'] = dictionary['imdb']['rating']['$numberInt']

            if dictionary['imdb'].get('votes'):
                dictionary['imdb']['votes'] = dictionary['imdb']['votes']['$numberInt']
            dictionary['imdb']['id'] = dictionary['imdb']['id']['$numberInt']

            if dictionary.get('tomatoes'):
                if dictionary['tomatoes'].get('viewer'):
                    if dictionary['tomatoes']['viewer'].get('rating'):
                        if dictionary['tomatoes']['viewer']['rating'].get('$numberInt'):
                            dictionary['tomatoes']['viewer']['rating'] = \
                                dictionary['tomatoes']['viewer']['rating']['$numberInt']
                        else:
                            dictionary['tomatoes']['viewer']['rating'] = \
                                dictionary['tomatoes']['viewer']['rating']['$numberDouble']

                    dictionary['tomatoes']['viewer']['numReviews'] = \
                        dictionary['tomatoes']['viewer']['numReviews']['$numberInt']
                dictionary['tomatoes']['lastUpdated'] = dictionary['tomatoes']['lastUpdated']['$date'][
                    '$numberLong']

            if dictionary.get('num_mflix_comments'):
                dictionary['num_mflix_comments'] = dictionary['num_mflix_comments']['$numberInt']
        data.append(dictionary)

    # created/switched to collection
    Collection = db["movies"]
    if isinstance(data, list):
        Collection.insert_many(data)
    else:
        Collection.insert_one(data)
