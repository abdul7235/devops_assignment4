FROM python:latest

ADD . /devops_assignment2_part4

WORKDIR /devops_assignment2_part4

RUN pip install -r requirements.txt

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --port 8000 --workers 1
