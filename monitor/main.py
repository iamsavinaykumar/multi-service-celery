import os
from celery import Celery

celery_app = Celery('tasks', broker=f'pyamqp://guest@{os.environ.get("RABBITMQ_HOST", "localhost")}//')

def event_monitor(app):
    def on_event(event):
        event_type = event.get('type')
        if event_type.strip() == 'worker-heartbeat':
            # print('------------------> worker heartbeat')
            pass
        else:
            print('---->', event_type)
            print(event)

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={'*': on_event})
        recv.capture(limit=None, timeout=None, wakeup=True)


if __name__ == '__main__':
    event_monitor(celery_app)