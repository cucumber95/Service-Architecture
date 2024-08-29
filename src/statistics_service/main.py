from flask import Flask, make_response
from kafka import KafkaConsumer
from clickhouse_driver import Client
import threading
import json
import statistics_service.queries as queries
import os
import grpc
from concurrent import futures
import logging

from statistics_service.proto.statistics_service_pb2 import GetStatsResponce, TaskStats, GetTopTasksResponce, UserStats, GetTopUsersResponce, Type
from statistics_service.proto.statistics_service_pb2_grpc import StatisticsServiceServicer, add_StatisticsServiceServicer_to_server


KAFKA_URL = 'kafka:9092'
clickhouse_client = Client(host='clickhouse', port=9000)
logging.basicConfig(level=logging.INFO)


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
        
        topics = consumer.topics()

        if not 'views_topic' in topics or not 'likes_topic' in topics :
            raise Exception("Topics are not available")

        for message in consumer:
            taskId = message.value['taskId']
            login = message.value['login']

            if message.topic == 'likes_topic':
                clickhouse_client.execute(queries.insert_like(taskId, login))
            else:
                clickhouse_client.execute(queries.insert_view(taskId, login))
    except:
        os._exit(1)

def restInit():
    app = create_app()
    app.run(host='0.0.0.0', port=8092)

class StatisticsServiceServer(StatisticsServiceServicer):
    def GetStats(self, request, context):
        taskId = request.taskId

        likes = clickhouse_client.execute(f"SELECT uniqExact(login) AS unique_logins FROM likes_stats WHERE taskId = {taskId} GROUP BY taskId")
        if likes:
            likes = likes[0][0]
        else:
            likes = 0

        views = clickhouse_client.execute(f"SELECT uniqExact(login) AS unique_logins FROM views_stats WHERE taskId = {taskId} GROUP BY taskId")
        if views:
            views = views[0][0]
        else:
            views = 0

        return GetStatsResponce(likes=likes, views=views)
    
    def GetTopTasks(self, request, context):
        type = request.type
        tasks = request.taskId

        if type == Type.LIKES:
            likes = clickhouse_client.execute(f"SELECT taskId, uniqExact(login) AS unique_logins FROM likes_stats WHERE taskId IN {tasks} GROUP BY taskId ORDER BY taskId DESC")
            
            if len(likes) < 5:
                for task in tasks:
                    fl = False
                    for l in likes:
                        if l[0] == task:
                            fl = True
                            break
                    if not fl:
                        likes.append((task, 0))
                    if len(likes) >= 5:
                        break

            result = list()
            for i in range (min(5, len(likes))):
                result.append(TaskStats(taskId=likes[i][0], count=likes[i][1]))
            return GetTopTasksResponce(tasks=result)
        else:
            views = clickhouse_client.execute(f"SELECT taskId, uniqExact(login) AS unique_logins FROM views_stats WHERE taskId IN {tasks} GROUP BY taskId ORDER BY taskId DESC")

            if len(views) < 5:
                for task in tasks:
                    fl = False
                    for l in views:
                        if l[0] == task:
                            fl = True
                            break
                    if not fl:
                        views.append((task, 0))
                    if len(views) >= 5:
                        break

            result = list()
            for i in range (min(5, len(views))):
                result.append(TaskStats(taskId=views[i][0], count=views[i][1]))
            return GetTopTasksResponce(tasks=result)

    def GetTopUsers(self, request, context):
        users = request.users
        cur_result = list()

        for user in users:
            likes = clickhouse_client.execute(f"SELECT uniqExact(taskId, login) AS unique_logins FROM likes_stats WHERE taskId IN {user.taskId}")
            cur_result.append((user.login, likes))

        cur_result.sort(key=lambda x: x[1], reverse=True)
        result = list()
        for i in range (min(3, len(cur_result))):
            result.append(UserStats(login=cur_result[i][0], likes=cur_result[i][1][0][0]))

        return GetTopUsersResponce(users=result)

def main():
    thread = threading.Thread(target=consumerInit)
    thread.start()

    thread = threading.Thread(target=restInit)
    thread.start()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    add_StatisticsServiceServicer_to_server(StatisticsServiceServer(), server)
    server.add_insecure_port('0.0.0.0:5050')
    server.start()
    server.wait_for_termination(timeout=None)

if __name__ == "__main__":
    main()