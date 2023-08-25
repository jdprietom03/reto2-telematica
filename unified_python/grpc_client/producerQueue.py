import pika
from dotenv import load_dotenv
import os

load_dotenv()
RMQ_HOST = os.getenv('RMQ_HOST')
RMQ_PORT = os.getenv('RMQ_PORT')
RMQ_USER = os.getenv('RMQ_USER')
RMQ_PASS = os.getenv('RMQ_PASS')
RMQ_EXCHANGE = os.getenv('RMQ_EXCHANGE')
RMQ_QUEUE = os.getenv('RMQ_QUEUE')


def RunAMQP(body):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RMQ_HOST, RMQ_PORT, '/', pika.PlainCredentials(RMQ_USER, RMQ_PASS)))
    channel = connection.channel()

    channel.queue_declare(queue=RMQ_QUEUE, durable=True)
    channel.basic_publish(exchange=RMQ_EXCHANGE, routing_key='', body=body)

    connection.close()