from flask.ext.restful import Resource, Api, reqparse
import models
import json

class MessageResource(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('message', type=str)
		self.args = self.parser.parse_args()

	def get(self):
		return json.dumps([
			{'message':msg.message, 'timestamp': str(msg.timestamp)}
			for msg in models.MessageDocument.objects
		])

	def post(self):
		message = self.args['message']	
		message_document = models.MessageDocument()
		message_document.message = message
		message_document.save()