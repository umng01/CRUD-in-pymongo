import pymongo 


if __name__ == "__main__":
    print("Hello")

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['umang']
    collection = db['mySampleCollection']


    prev = {"Name": "Alice"}
    nextt = {"$set": {"Location": "Europe"}} #use dollar set to update
    
    
    # collection.update_one(prev, nextt)

    # update all prev with next
    collection.update_many(prev, nextt)

    
    