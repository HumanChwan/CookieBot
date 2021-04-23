import mongoengine


class Emoji(mongoengine.Document):
    guild_id = mongoengine.IntField(required=True)
    _id = mongoengine.IntField(required=True)
    animated = mongoengine.BooleanField(required=True)
    name = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'NetData',
        'collection': 'Emoji'
    }
