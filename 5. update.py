import pymongo 


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['umang']
    collection = db['mySampleCollection']


    prev = {"Name": "Arjun Gupta"}
    nextt = {"$set": {"College": "NIT"}} #use dollar set to update
    
    
    # collection.update_one(prev, nextt)

    # update all prev with next
    collection.update_many(prev, nextt)

    
    