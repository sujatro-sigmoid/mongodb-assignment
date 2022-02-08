
from theaters.load_theaters_data import theatersData


def insert_theatre(collections, theaterId, location):
    collections.insert_one({'theaterId': theaterId,'location': location})


def top_cities_with_maximum_theatres(collections):
    dictionary = {}
    for i in collections.find():
        city = i['location']['address']['city']
        if dictionary.get(city):
            dictionary[city] +=1
        else:
            dictionary[city] = 1
    a = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return a[0:10]


def theatres_nearby_given_coordinates(collections,coord):
    dictionary = {}
    for i in collections.find():
        cord_data = i['location']['geo']['coordinates']
        x = float(coord[0]) - float(cord_data[0])
        y = float(coord[1]) - float(cord_data[1])
        x = round(x*x + y*y,5)
        if dictionary.get(x):
            dictionary[x].append(i['theaterId'])
        else:
            dictionary[x]=[]
            dictionary[x].append(i['theaterId'])
    a = dict(sorted(dictionary.items()))
    ans = []
    for k,v in a.items():
        ans += v
        if len(ans)+len(v)>10:
            x = 10-len(ans)
            ans += v[0:x]
        else:
            ans += v
        if len(ans) >= 10:
            break
    return ans



def theaters(db):
    collections = db['theaters']

    top_cities = top_cities_with_maximum_theatres(collections)
    print("Top 10 cities with maximum theatres")
    print(top_cities)

    lat = '-95.0000'
    lon = '35.0000'
    nearby_theatre = theatres_nearby_given_coordinates(collections,[lat,lon])
    print(f"Top 10 theatres nearby given coordinates eg: [{lat}, {lon}]")
    print(nearby_theatre)
