import mongoengine


class CoolGame(mongoengine.EmbeddedDocument):

    player_in_cool = mongoengine.BooleanField(required=True, default=False)
    tries = mongoengine.IntField(default=10)
    temp_random = mongoengine.ListField(required=False)
    total_played = mongoengine.IntField(required=True, default=0)
    total_won = mongoengine.IntField(required=True, default=0)
