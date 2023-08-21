# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# consumer.py
# Consume RabbitMQ queue

import pika
import os
from dotenv import load_dotenv

load_dotenv()
RMQ_HOST = os.getenv('RMQ_HOST')
RMQ_PORT = os.getenv('RMQ_PORT')
RMQ_USER = os.getenv('RMQ_USER')
RMQ_PASS = os.getenv('RMQ_PASS')

connection = pika.BlockingConnection(pika.ConnectionParameters(RMQ_HOST, RMQ_PORT, '/', pika.PlainCredentials(RMQ_USER, RMQ_PASS)))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f'{body} is received')
    
channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()