# myapp/models.py

from mongoengine import Document, StringField, IntField


class User(Document):
    _id = StringField(primary_key=True)
    name = StringField(required=True)
    age = IntField()
    # meta = {
    #     'collection': 'users',
    #     'indexes': [
    #         {'fields': ['_id'], 'unique': True}  # Enforce uniqueness on `_id`
    #     ]
    # }