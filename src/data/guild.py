import datetime
import mongoengine

from data.member import Member


class Guild(mongoengine.Document):
    date_joined = mongoengine.DateTimeField(default=datetime.datetime.now)
    _id = mongoengine.IntField(required=True)
    welcome_channel_id = mongoengine.IntField(default=None)
    member_list = mongoengine.EmbeddedDocumentListField(Member)
    prefix_acceptable = mongoengine.ListField(default=['cookie', 'ck'])

    meta = {
        'db_alias': 'NetData',
        'collection': 'Guilds'
    }
