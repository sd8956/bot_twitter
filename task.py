from celery import Celery
from bot import make_tweet


app = Celery('tweet',broker='amqp://admin:mypass@rabbitmq:5672')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls every 2 m.
    sender.add_periodic_task(20.0, publish.s(), name='add every 2')


@app.task
def publish():
    print('Publicando')
    make_tweet()
