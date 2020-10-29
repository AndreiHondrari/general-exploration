import time
import random
import eventlet
import socketio
from flask import Flask

# define the Flask app
flask_app = Flask(__name__)

# define the SocketIO wrapper
sio = socketio.Server(
    async_mode='eventlet',
    cors_allowed_origins='*'
)
app = socketio.WSGIApp(sio, flask_app)


# declare soem SIO events
@sio.event
def connect(sid, environ):
    print("\n----- CONNECT ", sid, end="\n\n")
    sio.emit('connected', data=f"Hello {sid}")

@sio.on('process-data')
def process_data(sid, data):
    print(f"\n----- PROCESS DATA {data}", end="\n\n")
    time.sleep(random.randint(1, 3))
    sio.emit('data-processing-done', data=random.randint(100, 1000))

@sio.event
def disconnect(sid):
    print('\n----- DISCONNECT ', sid, end="\n\n")

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
