FROM python:3.8-slim

WORKDIR /tasks_service
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY proto/ tasks_service/proto/
COPY server/ tasks_service/server/

ENTRYPOINT ["python", "-m", "tasks_service.server.main"]