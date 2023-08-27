import pika
from dotenv import load_dotenv
import os
import uuid

load_dotenv()
RMQ_HOST = os.getenv('RMQ_HOST')
RMQ_PORT = int(os.getenv('RMQ_PORT'))  # Convertimos a int ya que los puertos son números enteros
RMQ_USER = os.getenv('RMQ_USER')
RMQ_PASS = os.getenv('RMQ_PASS')
RMQ_EXCHANGE = os.getenv('RMQ_EXCHANGE')
RMQ_QUEUE = os.getenv('RMQ_QUEUE')

class AMQPRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RMQ_HOST, 
                port=RMQ_PORT, 
                credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASS)
            )
        )
        self.channel = self.connection.channel()
        
        # Declaramos una cola dinámica y efímera
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=RMQ_EXCHANGE,
            routing_key=RMQ_QUEUE,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=body)
        self.connection.process_data_events()
        return self.response

def RunAMQP(body):
    rpc_client = AMQPRpcClient()
    response = rpc_client.call(body)
    return response
