import pymongo 


if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['umang']
    collection = db['mySampleCollection']

    d1 = {
        '_id': 1,
        'Name': 'Umang Sharma',
        'RollNo': '45',
        'Branch': 'Information Technology',
        'College': 'KIET Group of Institutions',
        'Phone': 9876543210,
        'GPA': 9,
        'Gender': 'F'

    }
    d2 = {
        '_id': 2,
        'Name': 'Mehak Sharma',
        'RollNo': '50',
        'Branch': 'English Honours',
        'College': 'Ambedkar University',
        'Phone': 987657886,
        'GPA': 8,
        'Gender': 'F'

    }
    d3 = {
        '_id': 3,
        'Name': 'Vikhyat Sharma',
        'RollNo': '55',
        'Branch': 'CSE',
        'College': 'IIT',
        'Phone': 9343543210,
        'GPA': 10,
        'Gender': 'M'

    }
    d4 = {
        '_id': 4,
        'Name': 'Vansh Sharma',
        'RollNo': '15',
        'Branch': 'Business Administration',
        'College': 'JIMS',
        'Phone': 88363210,
        'GPA': 7,
        'Gender': 'M'

    }
    d5 = {
        '_id': 5,
        'Name': 'Arjun Gupta',
        'RollNo': '05',
        'Branch': 'Mechanical',
        'College': 'Jaypee Institute of Technology',
        'Phone': 898386543,
        'GPA': 9.8,
        'Gender': 'M'

    }
    d6 = {
        '_id': 6,
        'Name': 'Utkarsh',
        'RollNo': '13',
        'Branch': 'Computer Science',
        'College': 'IIT Patna',
        'Phone': 6383443210,
        'GPA': 8,
        'Gender': 'M'

    }

    insertThese = [
        d1,d2,d3,d4,d5,d6

    ]

    collection.insert_many(insertThese)


