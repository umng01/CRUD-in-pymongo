# https://www.codewithharry.com/blogpost/mongodb-cheatsheet

import pymongo 


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['umang']
    collection = db['mySampleCollection']
    

