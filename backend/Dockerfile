FROM python:3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /backend

EXPOSE 8000

COPY ./ /backend

ENV IN_DOCKER Yes

RUN pip install -r requirements.txt

CMD ["python", "main.py"]