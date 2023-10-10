import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth import authenticate, login
ip_to_socket = {}
ips=[]
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='test'
        self.user_id = self.scope["user"].id
        ips.append(self.scope['client'][0]+'.'+str(self.scope['client'][1]) )
        ip_to_socket[self.scope['client'][0]+'.'+str(self.scope['client'][1]) ] = self
        print(ips)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    """
    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        if (message[0]=="G") and len(ips)>=2:
            recipient_socket = ip_to_socket[ips[1]]
            async_to_sync(recipient_socket.send(text_data=json.dumps({
                    'type': 'chat',
                    'message': message
                }))
            )
        else:

            recipient_socket = ip_to_socket[ips[0]]
            async_to_sync(recipient_socket.send(text_data=json.dumps({
                    'type': 'chat',
                    'message': message
                }))
            )
    
    """
    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        sender_ip = self.scope['client'][0]+'.'+str(self.scope['client'][1])
        if sender_ip==ips[0]:
            recipient_socket = ip_to_socket[ips[1]]
            async_to_sync(recipient_socket.send(text_data=json.dumps({
                    'type': 'chat',
                    'message': message
                }))
            )
        else:

            recipient_socket = ip_to_socket[ips[0]]
            async_to_sync(recipient_socket.send(text_data=json.dumps({
                    'type': 'chat',
                    'message': message
                }))
            )


    """
            async_to_sync(self.channel_layer.group_send)(
                recipient_ip,
                {
                    'type':'chat_message',
                    'message':message
                }
            )
    """
 
    def chat_message(self,event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':"chat",
            'message':message
            
        }))
    """
    def binary_message(self, message):
        # Handle incoming binary frames here
        #await self.send_binary(message.content)
        print("executed here")
        self.send(text_data=json.dumps({"message": "Binary message received"}))
    """

        


"""
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!'
        }))

    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        print('Message:', message)

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
"""