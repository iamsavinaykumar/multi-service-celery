import os
from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger

celery_app = Celery('tasks', broker=f'pyamqp://guest@{os.environ.get("RABBITMQ_HOST", "localhost")}//')
logger = get_task_logger(__name__)

@celery_app.task(name="task1", bind=True)
def task1(self, *args, **kwargs):
    for i in range(1, 20):
        logger.info(f'----> Running task 1: Iteration {i} of 20')
        logger.info(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        print(self)
        if i==10:
            self.update_state(state='PROGRESS', meta={'current': i, 'total': 20})
        if i==15:
            self.update_state(state="ENRICHMENT", meta={'current': i, 'total': 20})
        sleep(2)
    return True

