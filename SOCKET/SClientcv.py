import websocket
import json
import cv2
import base64
import threading
import time


# Define the WebSocket server URL
server_url = "ws://127.0.0.1:8000/ws/socket-server/" 
# Create a WebSocket connection
ws = websocket.WebSocket()
ws.connect(server_url)
cap = cv2.VideoCapture(0)
# Send a message to the server
message = "Hello, Server!"
message = {"message":message}
message= json.dumps(message)

def thread_function_1():
    while True:
        ret, frame = cap.read()
        _, buffer = cv2.imencode('.jpg', frame)
        message = base64.b64encode(buffer).decode('utf-8')
        message = {"message":message}
        message= json.dumps(message)
        ws.send(message)
        # Send the frame through the WebSocket connection
        #ws.send_binary(frame_bytes)
        #response = ws.recv()
        #print("Received:", response)


def thread_function_2():
    while True:
        response = ws.recv()
        print("Received:", response)



thread1 = threading.Thread(target=thread_function_1)
thread2 = threading.Thread(target=thread_function_2)

# Start the threads
thread1.start()
thread2.start()

"""
# Receive and print messages from the server
while True:
    ret, frame = cap.read()
    _, buffer = cv2.imencode('.jpg', frame)
    message = base64.b64encode(buffer).decode('utf-8')
    message = {"message":message}
    message= json.dumps(message)
    ws.send(message)
    # Send the frame through the WebSocket connection
    #ws.send_binary(frame_bytes)
    #response = ws.recv()
    #print("Received:", response)

# Close the WebSocket connection when done
ws.close()
"""