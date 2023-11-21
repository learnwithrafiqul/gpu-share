import socketio
import time

# Initialize the Socket.IO client
sio = socketio.Client()

# Connect to the server
sio.connect('http://127.0.0.1:5000')

# Event handler for receiving messages from App1
@sio.event
def message_from_app1(message):
    print('Received message from App1:', message)

# Event handler for receiving messages from App2
@sio.event
def message_from_app2(message):
    print('Received message from App2:', message)

# Send a message to App1 every second
while True:
    time.sleep(1)
    sio.emit('message_from_app1', 'Hello from Client')
