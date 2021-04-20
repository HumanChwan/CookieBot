import mongoengine

from data.cool_game import CoolGame


class Member(mongoengine.EmbeddedDocument):
    member_Id = mongoengine.StringField(required=True)
    cool_game_data = mongoengine.EmbeddedDocumentField(CoolGame)
