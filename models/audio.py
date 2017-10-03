from mongoengine import Document, StringField

class Audio(Document):
    search_terms = StringField()
    title = StringField()
    url = StringField()
    thumbnail = StringField()
    description = StringField()
