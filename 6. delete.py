import pymongo 


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['umang']
    collection = db['mySampleCollection']


    rec = {"Name": "Bob"}
    collection.delete_one(rec)

    x = collection.delete_many(rec)
    print(x.deleted_count)

    
    