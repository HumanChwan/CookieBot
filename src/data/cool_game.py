import mongoengine


class CoolGame(mongoengine.EmbeddedDocument):

    PlayerInCool = mongoengine.BooleanField(required=True, default=False)
    TotalPlayed = mongoengine.IntField(required=True, default=0)
    TotalWon = mongoengine.IntField(required=True, default=0)
