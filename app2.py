from flask import Flask, render_template
from flask_socketio import SocketIO

app2 = Flask(__name__)
socketio = SocketIO(app2)

@app2.route('/')
def index():
    return "App2 is running with Socket.IO"

@socketio.on('message_from_app2')
def handle_message(message):
    print('Received message from App2:', message)
    socketio.emit('message_from_app1', message)

if __name__ == '__main__':
    socketio.run(app2, debug=True)
