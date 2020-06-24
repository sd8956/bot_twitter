FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#ENTRYPOINT celery -A task worker -l info
#ENTRYPOINT celery worker --loglevel=info -A task --beat
ENTRYPOINT celery -A task worker -B -l info