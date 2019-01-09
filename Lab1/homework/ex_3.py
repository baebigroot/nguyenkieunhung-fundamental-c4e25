from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
post = db["posts"]

import datetime
new_post = {
    "title" :"Ồ ô ố ô",
    "author": "Nhung B",
    "text": "Ồ ố ô ố ô",
    }

post.insert_one(new_post)
client.close()