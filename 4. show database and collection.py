import pymongo 


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    database = client.list_database_names()
    print(database)

    col = client['umang']
    print(col.list_collection_names)



    