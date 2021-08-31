FROM python:3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /backend

EXPOSE 8000

RUN pip install -r requirements.txt

COPY ./ /backend

ENV IN_DOCKER Yes


CMD ["python", "main.py"]