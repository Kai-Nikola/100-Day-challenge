import json

movies = [
    {
        "title": "Your Name",
        "released": 2016,
        "Genre": "Romance"
    }
]

dict_to_json = json.dumps(movies)
print(dict_to_json)
print(type(dict_to_json))