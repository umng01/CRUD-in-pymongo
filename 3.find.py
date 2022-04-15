import pymongo 


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['umang']
    collection = db['mySampleCollection']

    # one = collection.find_one({'Name': 'Alice'})
    allDocs = collection.find({'Name': 'Utkarsh'}, {'Name':1, 'Phone': 1, '_id': 0}) # include only name
    for item in allDocs: 
        print(item)
    # print(allDocs)

    print()

    allDocs = collection.find({'Name': 'Umang Sharma'}, {'_id': 0}) 
    for item in allDocs: 
        print(item)
    # print(allDocs)
    # print("Count of all the documents with name as Umang Sharma")
    # print(allDocs.count)
    