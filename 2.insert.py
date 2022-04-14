import pymongo 


if __name__ == "__main__":
    print("Hello")

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['umang']
    collection = db['mySampleCollection']
    # dictionary = {'name': 'Umang', 'marks': 50}
    # collection.insert_one(dictionary)

    # dictionary2 = {'name': 'UmangSh', 'marks': 60}
    # collection.insert_one(dictionary2)

    # dictionary3 = {'name': 'UmangSharma', 'marks': 70}
    # collection.insert_one(dictionary3)

    insertThese = [

        {'_id': '1', 'Name':'Alice', 'Location': 'Delhi', 'Marks': 67},
        {'_id': '2', 'Name':'Bob', 'Location': 'Delhi', 'Marks': 68},
        {'_id': '3', 'Name':'Mariya', 'Location': 'Delhi', 'Marks': 69},
        {'_id': '4', 'Name':'Ram', 'Location': 'Delhi', 'Marks': 70}

    ]

    collection.insert_many(insertThese)














