FROM python:3.8-slim

WORKDIR /statistics_service

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY queries.py .

ENTRYPOINT ["python", "-m", "main"]