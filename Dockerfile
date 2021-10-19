FROM python:3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV IN_DOCKER Yes

CMD ["python", "main.py"]