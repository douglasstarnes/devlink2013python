from flask import Flask, request, render_template, redirect, url_for
from flask.ext.restful import Resource, Api, reqparse
import mongoengine
import datetime
import json
import models
import api as restapi

app = Flask(__name__)
app.debug = True

@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html', 
		messages=[
			{'message':message.message, 'timestamp': message.timestamp.strftime('%b %d %Y %I:%M:%S %p')} 
				for message in models.MessageDocument.objects
			]
		)

@app.route('/write_message', methods=['GET', 'POST',])
def write_message():
	if request.method == 'GET':
		return render_template('write_message.html')
	else:
		message = request.form['message']
		message_document = models.MessageDocument()
		message_document.message = message
		message_document.save()
		return redirect(url_for('index'))

@app.route('/to_json')
def to_json():
	return json.dumps([
			{'message': msg.message, 'timestamp': msg.timestamp.strftime('%b %d %Y  %I:%M:%S %p')}
			for msg in models.MessageDocument.objects
		])

@app.route('/test_api')
def test_api():
	return render_template('test_api.html')

api = Api(app)

api.add_resource(restapi.MessageResource, '/messages')

if __name__ == '__main__':
	mongoengine.connect('flask_demo')
	app.run(port=5001)