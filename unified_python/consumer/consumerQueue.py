# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# consumer.py
# Consume RabbitMQ queue

import pika
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
RMQ_HOST = os.getenv('RMQ_HOST')
RMQ_PORT = os.getenv('RMQ_PORT')
RMQ_USER = os.getenv('RMQ_USER')
RMQ_PASS = os.getenv('RMQ_PASS')

dir = "./assets"

connection = pika.BlockingConnection(pika.ConnectionParameters(RMQ_HOST, RMQ_PORT, '/', pika.PlainCredentials(RMQ_USER, RMQ_PASS)))
channel = connection.channel()

def callback(ch, method, properties, body):
    response = []

    for file_name in os.listdir(dir):
        file_info = {}
        file_info["name"] = file_name
        file_path = os.path.join(dir, file_name)

        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            time = os.path.getmtime(file_path)
            timestamp = datetime.datetime.fromtimestamp(time)
            formatted_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")

            file_info["size"] = size
            file_info["timestamp"] = formatted_date

            response.append(file_info)

    print(f'The response is : {response}')
    
channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()