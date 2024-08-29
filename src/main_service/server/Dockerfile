FROM python:3.8-slim

WORKDIR /main_service/server
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY auth/ auth/

ENTRYPOINT ["python", "-m", "main"]