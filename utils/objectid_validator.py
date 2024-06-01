from bson import ObjectId as BsonObjectId

class ObjectIdValidator(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not BsonObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return BsonObjectId(v)
