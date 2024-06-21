FROM python:3.11

#WORKDIR /usr/src/app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ENV_FILE .env

CMD ["python", "./main.py"]