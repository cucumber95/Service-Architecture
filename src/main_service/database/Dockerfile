FROM python:3.8-slim

WORKDIR /main_service/database
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY interact.py .
COPY database.db .

ENTRYPOINT ["python", "-m", "main"]