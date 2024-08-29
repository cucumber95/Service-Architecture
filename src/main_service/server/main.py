from flask import Flask, request, make_response
import json
import hashlib
import jwt
import requests
import grpc

from google.protobuf import json_format 
from tasks_service.proto.tasks_service_pb2 import CreateTaskRequest, UpdateTaskRequest, DeleteTaskRequest, GetTaskRequest, GetTasksListRequest, Statuses
from tasks_service.proto import tasks_service_pb2_grpc
from statistics_service.proto.statistics_service_pb2 import GetStatsRequest, Type, GetTopTasksRequest, UserTasks, GetTopUsersRequest
from statistics_service.proto import statistics_service_pb2_grpc
from kafka_producer import sendView, sendLike

import logging
logging.basicConfig(level=logging.INFO)


MAIN_DB = 'http://database:8091'


def get_hash(cur_str):
    return hashlib.md5(cur_str.encode()).hexdigest()

def get_cookie(login, private):
    return jwt.encode({'login': login}, private, 'RS256')

def decode_cookie(kuka, public):
    return jwt.decode(kuka, public, ['RS256'])

def update_data(login, data):
    data['login'] = login
    response = requests.post(f'{MAIN_DB}/data', data=json.dumps(data))
    return response.json()

def create_app(private, public, tasks_stub, statistics_stub) -> Flask:
    app = Flask(__name__)

    @app.route('/signup', methods=['POST'])
    def signup():
        body = json.loads(request.data)
        login = body['login']
        password = body['password']

        response = requests.get(f'{MAIN_DB}/password', data=json.dumps({'login': login}))
        if response.status_code == 200:
            return make_response('Пользователь уже существует\n', 403)
        
        requests.post(f'{MAIN_DB}/password', data=json.dumps({'login': login, 'password': get_hash(f'{login}{password}')}))
        requests.post(f'{MAIN_DB}/data/init', data=json.dumps({'login': login}))
        return make_response('Успешная регистрация\n', 200, {'Set-Cookie': f'jwt={get_cookie(login, private)}'})

    @app.route('/login', methods=['GET'])
    def login():
        body = json.loads(request.data)
        login = body['login']
        password = body['password']

        response = requests.get(f'{MAIN_DB}/password', data=json.dumps({'login': login}))
        if response.status_code == 403:
            return make_response('Пользователя с таким логином не существует\n', 403)
        
        cur_password = response.text
        
        if not cur_password == get_hash(f'{login}{password}'):
            return make_response('Неверный пароль к логину\n', 401)

        return make_response('Успешная авторизация\n', 200, {'Set-Cookie': f'jwt={get_cookie(login, private)}'})
    
    @app.route('/update', methods=['PUT'])
    def update():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
            response = update_data(login, json.loads(request.data))
            return make_response(f'Успешное обновление данных пользователя\n{response}\n', 200)
        except:
            return make_response('Невалидная кука\n', 401)
        
    @app.route('/tasks/create', methods=['POST'])
    def tasks_create():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
        
        body = json.loads(request.data)
        try:
            title = body['title']
            content = body['content']
        except:
            return make_response('В запросе нет title или content\n', 403)
        
        status = 0
        if body.get('status', None):
            status = body['status']
        
        task = tasks_stub.CreateTask(CreateTaskRequest(authorLogin=login, title=title, content=content, status=status))
        status = Statuses.Name(task.status)
        task = json_format.MessageToDict(task)
        task['status'] = status
        return make_response(f"Успешное создание задачи\n{task}\n", 200)
    
    @app.route('/tasks/update', methods=['PUT'])
    def tasks_update():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
        
        body = json.loads(request.data)
        try:
            taskId = body['taskId']
        except:
            return make_response('В запросе нет taskId\n', 403)
        
        if not body.get('title', None) and not body.get('content', None) and not body.get('status', None):
            return make_response('Невалидный запрос', 404)
        
        resp = tasks_stub.UpdateTask(UpdateTaskRequest(taskId=taskId, authorLogin=login, title=body.get('title', None), content=body.get('content', None), status=body.get('status', None)))
        if not resp.isUpdated:
            return make_response('Невалидный taskId\n', 405)
        
        task = resp.task
        status = Statuses.Name(task.status)
        task = json_format.MessageToDict(task)
        task['status'] = status
        return make_response(f"Успешное обновление задачи\n{task}\n", 200)
    
    @app.route('/tasks/delete', methods=['DELETE'])
    def tasks_delete():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
        
        body = json.loads(request.data)
        try:
            taskId = body['taskId']
        except:
            return make_response('В запросе нет taskId\n', 403)
        
        resp = tasks_stub.DeleteTask(DeleteTaskRequest(taskId=taskId, authorLogin=login))
        if not resp.IsDeleted:
            return make_response('Невалидный taskId\n', 405)
        
        return make_response("Успешное удаление задачи\n", 200)
    
    @app.route('/tasks/get', methods=['GET'])
    def tasks_get():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
        
        body = json.loads(request.data)
        try:
            taskId = body['taskId']
        except:
            return make_response('В запросе нет taskId\n', 403)
        
        resp = tasks_stub.GetTask(GetTaskRequest(taskId=taskId, authorLogin=login))
        if not resp.isAccessible:
            return make_response('Невалидный taskId\n', 406)
        
        task = resp.task
        status = Statuses.Name(task.status)
        task = json_format.MessageToDict(task)
        task['status'] = status
        return make_response(f"Успешное получение задачи\n{task}\n", 200)
    
    @app.route('/tasks/get_page', methods=['GET'])
    def tasks_get_page():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
        
        body = json.loads(request.data)
        try:
            authorLogin = body['authorLogin']
            pageSize = body['pageSize']
            page = body['page']
        except:
            return make_response('В запросе нет authorLogin, pageSize или page\n', 403)
        
        if pageSize <= 0:
            return make_response('pageSize должно быть положительным числом', 406)
        
        tasks = tasks_stub.GetTasksList(GetTasksListRequest(authorLogin=authorLogin, pageSize=pageSize, page=page))
        tasks_result = list()

        for task in tasks.tasks:
            status = Statuses.Name(task.status)
            task_result = json_format.MessageToDict(task)
            task_result['status'] = status
            tasks_result.append(task_result)

        return make_response(f"Успешное получение страницы с задачами\n{tasks_result}\n", 200)
    
    @app.route('/statistics/send_view', methods=['POST'])
    def statistics_send_view():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)

        body = json.loads(request.data)
        try:
            taskId = body['taskId']
        except:
            return make_response('В запросе нет taskId\n', 403)

        sendView(taskId, login)
        return make_response("Запрос о просмотре успешно отправлен\n", 200)
    
    @app.route('/statistics/send_like', methods=['POST'])
    def statistics_send_like():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)
        
        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)

        body = json.loads(request.data)
        try:
            taskId = body['taskId']
        except:
            return make_response('В запросе нет taskId\n', 403)

        sendLike(taskId, login)
        return make_response("Запрос о лайке успешно отправлен\n", 200)
    
    @app.route('/statistics/get_stats', methods=['GET'])
    def statistics_get_stats():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)

        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
    
        body = json.loads(request.data)
        try:
            taskId = body['taskId']
        except:
            return make_response('В запросе нет taskId\n', 403)
        
        resp = tasks_stub.GetTask(GetTaskRequest(taskId=taskId, authorLogin=login))
        if not resp.isAccessible:
            return make_response('Невалидный taskId\n', 406)
        
        response = statistics_stub.GetStats(GetStatsRequest(taskId=taskId))
        ans = {'taskId': taskId, 'likes': response.likes, 'views': response.views}

        return make_response(f'Успешное получение статистики по задаче\n{ans}\n', 200)
    
    @app.route('/statistics/get_top_tasks', methods=['GET'])
    def statistics_get_top_tasks():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)

        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
    
        body = json.loads(request.data)
        try:
            type = body['type']
        except:
            return make_response('В запросе нет type\n', 403)
        
        logins = json.loads(requests.get(f'{MAIN_DB}/logins').text)
        tasks = list()
        for login in logins:
            cur_tasks = tasks_stub.GetTasksList(GetTasksListRequest(authorLogin=login, pageSize=0, page=1))
            for task in cur_tasks.tasks:
                task_result = json_format.MessageToDict(task)
                tasks.append(int(task_result['id']))

        response = statistics_stub.GetTopTasks(GetTopTasksRequest(type=type, taskId=tasks))
        result = list()

        for task in response.tasks:
            cur_result = json_format.MessageToDict(task)
            if not cur_result.get('count', None):
                cur_result['count'] = 0
            result.append(cur_result)

        return make_response(f'Успешное получение топа задач\n{result}\n')
    
    @app.route('/statistics/get_top_users', methods=['GET'])
    def statistics_get_top_users():
        cookie = request.headers.get('Cookie', None)
        if not cookie:
            return make_response('Нет куки\n', 400)

        cookie = cookie[4:]
        try:
            result = decode_cookie(cookie, public)
            login = result['login']
        except:
            return make_response('Невалидная кука\n', 401)
        
        logins = json.loads(requests.get(f'{MAIN_DB}/logins').text)
        users = list()
        for login in logins:
            cur_tasks = tasks_stub.GetTasksList(GetTasksListRequest(authorLogin=login, pageSize=0, page=1))
            cur_tasks_list = list()
            for task in cur_tasks.tasks:
                task_result = json_format.MessageToDict(task)
                cur_tasks_list.append(int(task_result['id']))

            users.append(UserTasks(login=login, taskId=cur_tasks_list))

        response = statistics_stub.GetTopUsers(GetTopUsersRequest(users=users))
        result = list()

        for user in response.users:
            cur_result = json_format.MessageToDict(user)
            if not cur_result.get('likes', None):
                cur_result['likes'] = 0
            result.append(cur_result)

        return make_response(f'Успешное получение топа пользователей\n{result}\n')
        
            
    return app


def main():
    chanel = grpc.insecure_channel("tasks_server:5051")
    tasks_stub = tasks_service_pb2_grpc.TaskServiceStub(chanel)

    chanel = grpc.insecure_channel("statistics_server:5050")
    statistics_stub = statistics_service_pb2_grpc.StatisticsServiceStub(chanel)

    with open('auth/signature.pem', 'r') as f:
        private = f.read()
    with open('auth/signature.pub', 'r') as f:
        public = f.read()

    app = create_app(private, public, tasks_stub, statistics_stub)
    app.run(host='0.0.0.0', port=8090)

if __name__ == "__main__":
    main()

        




