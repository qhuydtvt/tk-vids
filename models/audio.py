from mongoengine import Document, StringField

class Audio(Document):
    search_terms = StringField()
    title = StringField()
    url = StringField()
    thumbnail = StringField()
    description = StringField()

    def to_dict(self):
        return {
            'search_terms': self.search_terms,
            'url': self.url,
            'thumbnail': self.thumbnail,
            'description': self.description
        }
