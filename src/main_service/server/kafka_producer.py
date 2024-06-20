from kafka import KafkaProducer
import json

KAFKA_URL = 'kafka:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_URL, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def sendView(taskId):
    producer.send('views_topic', {'taskId': taskId})

def sendLike(taskId):
    producer.send('likes_topic', {'taskId': taskId})


