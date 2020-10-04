from pymongo import MongoClient
 
# Creating connection to db on localhost
client = MongoClient('mongodb://localhost:27017')

# Creates the database
db = client['pymongo_test']

posts = db.posts

post_data = {
    'title': 'Python and MongoDB',
    'content': 'Learning about Python and MongoDB',
    'author': 'Jeff'
}

# Insert one document at a time
result = posts.insert_one(post_data)

print(f"One post: {result.inserted_id}")

post1, post2, post3 = {
    'title': 'Post One',
    'content': 'Post One about Python and MongoDB',
    'author': 'Jeff'
}, {
    'title': 'Post Two',
    'content': 'Post Two about Python and MongoDB',
    'author': 'Jeff'
}, {
    'title': 'Post Three',
    'content': 'Post Two about Python and MongoDB',
    'author': 'Jeff'
}

# Inserting multiple documents at once
second_insert_result = posts.insert_many([post1, post2, post3])

[print(f"Post Id: {id}") for id in second_insert_result.inserted_ids]

