from pyramid_mongoengine import MongoEngine

db = MongoEngine()


class Task(db.Document):
    name = db.StringField(required=True, max_length=200)
    category = db.StringField(requred=True, max_length=200)
    score = db.StringField(requred=True, max_length=20)
    created_at = db.DateTimeField(auto_now_add=True)
    updated_at = db.DateTimeField(auto_now=True)
