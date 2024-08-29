FROM python:3.8-slim

WORKDIR /main_service/server
COPY /main_service/server/requirements.txt .
RUN pip install -r requirements.txt

COPY /main_service/server/main.py .
COPY main_service/server/auth/ auth/
COPY tasks_service/proto/ tasks_service/proto/

ENTRYPOINT ["python", "-m", "main"]