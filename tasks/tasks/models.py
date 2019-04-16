import mongoengine


class Task(mongoengine.Document):
    name = mongoengine.StringField(required=True, max_length=200)
    theme = mongoengine.StringField(requred=True, max_length=200)
    liked = mongoengine.StringField(requred=True, max_length=10)
