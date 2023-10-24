from mongoengine import *
import datetime


class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)


connect("mongoengine_test", host="localhost", port=27017)

post = Post(title="Learning MongoDb", content="Here is some content", author="Jeff")

post.save()
print(f"Title: {post.title}")
post.title = "This is the new updated content"
post.save()
print(f"Title: {post.title}")
