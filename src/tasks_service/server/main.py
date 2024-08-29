from retry import retry
import psycopg2
import grpc
from concurrent import futures
 
from tasks_service.proto.tasks_service_pb2 import ITask, UpdateTaskResponse, DeleteTaskResponse, GetTaskResponse, GetTasksListResponse
from tasks_service.proto.tasks_service_pb2_grpc import TaskServiceServicer, add_TaskServiceServicer_to_server
import tasks_service.server.queries as queries


conn = psycopg2.extensions.connection


class TaskServiceServer(TaskServiceServicer):
    def CreateTask(self, request, context):
        authorLogin = request.authorLogin
        title = request.title
        content = request.content
        status = request.status

        with conn.cursor() as cursor:
            cursor.execute(queries.insert(authorLogin=authorLogin, title=title, content=content))
            id = cursor.fetchone()[0]

        return ITask(id=id, title=title, content=content, status=status)
        
    def UpdateTask(self, request, context):
        id = request.taskId
        authorLogin = request.authorLogin
        title = request.title
        content = request.content
        status = request.status

        with conn.cursor() as cursor:
            cursor.execute(queries.get_authorLogin(id))
            real_login = cursor.fetchone()

            if not real_login or not real_login[0] == authorLogin:
                return UpdateTaskResponse(isUpdated=False)
            
            cursor.execute(queries.update(id, title, content, status))
            cursor.execute(queries.select_task(id))
            task = cursor.fetchone()
        
        return UpdateTaskResponse(isUpdated=True, task=ITask(id=id, title=task[2], content=task[3], status=task[4]))

    def DeleteTask(self, request, context):
        id = request.taskId
        authorLogin = request.authorLogin

        with conn.cursor() as cursor:
            cursor.execute(queries.get_authorLogin(id))
            real_login = cursor.fetchone()

            if not real_login or not real_login[0] == authorLogin:
                return DeleteTaskResponse(IsDeleted=False)
            
            cursor.execute(queries.delete(id))

        return DeleteTaskResponse(IsDeleted=True)
    
    def GetTask(self, request, context):
        id = request.taskId
        authorLogin = request.authorLogin

        with conn.cursor() as cursor:
            cursor.execute(queries.get_authorLogin(id))
            real_login = cursor.fetchone()

            if not real_login or not real_login[0] == authorLogin:
                return GetTaskResponse(isAccessible=False)
            
            cursor.execute(queries.select_task(id))
            task = cursor.fetchone()

        return GetTaskResponse(isAccessible=True, task=ITask(id=id, title=task[2], content=task[3], status=task[4]))
    
    def GetTasksList(self, request, context):
        authorLogin = request.authorLogin
        pageSize = request.pageSize
        page = request.page

        with conn.cursor() as cursor:
            cursor.execute(queries.select_all_tasks(authorLogin))
            tasks = cursor.fetchall()

            tasks = [ITask(id=task[0], title=task[2], content=task[3], status=task[4]) for task in tasks]

        if len(tasks) >= pageSize * page:
            return GetTasksListResponse(tasks=tasks[pageSize * (page - 1):pageSize * page])
        elif len(tasks) >= pageSize * (page - 1):
            return GetTasksListResponse(tasks=tasks[pageSize * (page - 1):])
        else:
            return GetTasksListResponse(tasks=[])



@retry(delay=5.0, max_delay=20.0)
def create_connection():
    return psycopg2.connect(dbname='tasks_db', user='tasks_service_login', password='megapassword52fortasksservice', host='tasks_database', port='5432')

        
def main():
    global conn
    conn = create_connection()
    
    with conn.cursor() as cursor:
        cursor.execute(queries.create())

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    add_TaskServiceServicer_to_server(TaskServiceServer(), server)
    server.add_insecure_port('0.0.0.0:5050')
    server.start()
    server.wait_for_termination(timeout=None)


if __name__ == '__main__':
    main()