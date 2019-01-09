uri = "mongodb://admin:admin1@ds149754.mlab.com:49754/nhungs"

#1. Connect to mlab
from pymongo import MongoClient
client = MongoClient(uri)

#2. Get a database
db = client.get_database()

#3. Get a collection
test_collection = db["test"]

#4. Create a document
# #import datetime
test = {"title": "bim bim hành", #field title
        "content": "cũng ngon nhưng chưa ăn", #field content
}

# #5. Insert document
# test_collection.insert_one(test)


#6. Querying
# test_list = test_collection.find() #cursor
# first_test = test_list[0]
# print(first_test)

for test in test_collection.find():
    print(test) 

#Exit
client.close()
