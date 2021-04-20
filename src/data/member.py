import mongoengine

from data.cool_game import CoolGame


class Member(mongoengine.EmbeddedDocument):
    m_id = mongoengine.IntField(required=True)
    cool_game_data = mongoengine.EmbeddedDocumentField(CoolGame)
