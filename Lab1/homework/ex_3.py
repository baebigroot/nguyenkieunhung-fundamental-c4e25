from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
post = db["posts"]

import datetime
new_post = {
    "title" :"C4E25 ồ ố ô",
    "author": "Nhung B",
    "content": "Ồ ô ô ố ô, ồ ô ô ố ô, ồ ô ô ố ô ô ô ô",
    }

post.insert_one(new_post)
client.close()