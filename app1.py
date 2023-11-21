from flask import Flask, render_template
from flask_socketio import SocketIO

app1 = Flask(__name__)
socketio = SocketIO(app1)

@app1.route('/')
def index():
    return "App1 is running with Socket.IO"

@socketio.on('message_from_app1')
def handle_message(message):
    print('Received message from App1:', message)
    socketio.emit('message_from_app2', message)

if __name__ == '__main__':
    socketio.run(app1, debug=True)
