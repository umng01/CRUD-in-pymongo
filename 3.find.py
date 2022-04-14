import pymongo 


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['umang']
    collection = db['mySampleCollection']

    # one = collection.find_one({'Name': 'Alice'})
    allDocs = collection.find({'Name': 'Alice'}, {'Name':1, '_id': 0}) # include only name
    for item in allDocs: 
        print(item)
    print(allDocs)

    allDocs = collection.find({'Name': 'Alice'}, {'Name':0, '_id': 0}) # exclude only name
    for item in allDocs: 
        print(item)
    print(allDocs)
    print(allDocs.count())
    