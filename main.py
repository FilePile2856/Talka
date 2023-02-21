from flask import Flask, render_template
from flask_socketio import SocketIO
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['chat']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received')

@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    #print('received event: ' + str(json))
    socketio.emit('res', json, callback=messageReceived)
    if json != {'data': 'User Connected'}:
        print(json['user_name'])
        print(json['message'])
        collection = db['test']
        collection.insert_one(json)


if __name__ == '__main__':
    socketio.run(app, debug=False, port=8000)