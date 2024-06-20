from flask import Flask, make_response
from kafka import KafkaConsumer
from clickhouse_driver import Client
import threading
import json
import queries
import os


KAFKA_URL = 'kafka:9092'
clickhouse_client = Client(host='clickhouse', port=9000)


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def ping():
        return make_response("Hello from statistics service!\n", 200)

    return app

def consumerInit():
    try:
        clickhouse_client.execute(queries.drop_likes_table())
        clickhouse_client.execute(queries.drop_views_table())
        clickhouse_client.execute(queries.create_likes_table())
        clickhouse_client.execute(queries.create_views_table())

        consumer = KafkaConsumer(
            'views_topic', 'likes_topic',
            bootstrap_servers=KAFKA_URL,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')))

        for message in consumer:
            taskId = message.value['taskId']

            if message.topic == 'likes_topic':
                clickhouse_client.execute(queries.insert_like(taskId))
            else:
                clickhouse_client.execute(queries.insert_view(taskId))
    except:
        os._exit(1)

def main():
    thread = threading.Thread(target=consumerInit)
    thread.start()

    app = create_app()
    app.run(host='0.0.0.0', port=8092)

if __name__ == "__main__":
    main()