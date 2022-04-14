# https://www.codewithharry.com/blogpost/mongodb-cheatsheet

import pymongo 


if __name__ == "__main__":
    print("Hello")

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['umang']
    collection = db['mySampleCollection']
    

