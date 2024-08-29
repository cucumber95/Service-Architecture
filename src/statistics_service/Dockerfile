FROM python:3.8-slim

WORKDIR /

COPY statistics_service/requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir statistics_service

COPY statistics_service/main.py /statistics_service/main.py
COPY statistics_service/queries.py /statistics_service/queries.py
COPY statistics_service/proto/ /statistics_service/proto/

ENTRYPOINT ["python", "-m", "statistics_service.main"]