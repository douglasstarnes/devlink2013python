import mongoengine
import datetime

class MessageDocument(mongoengine.Document):
	message = mongoengine.StringField()
	timestamp = mongoengine.DateTimeField(default=datetime.datetime.now)