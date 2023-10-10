import websocket
import json
# Define the WebSocket server URL
server_url = "ws://127.0.0.1:8000/ws/socket-server/" 
# Create a WebSocket connection
ws = websocket.WebSocket()
ws.connect(server_url)

# Send a message to the server
message = "Hello, Server!"
message = {"message":message}
message= json.dumps(message)
ws.send(message)

# Receive and print messages from the server
while True:
    response = ws.recv()
    print("Received:", response)

# Close the WebSocket connection when done
ws.close()