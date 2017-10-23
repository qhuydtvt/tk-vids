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
            'thumbnail': self.thumbnail
        }

    @classmethod
    def exists(cls, search_terms):
        return Audio.objects(search_terms=search_terms).first() is not None

    @classmethod
    def save_from_dict(cls, search_terms, audio_info):
        audio = Audio(search_terms=search_terms, url=audio_info["url"], thumbnail=audio_info["thumbnail"])
        audio.save()
