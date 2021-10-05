import os
from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger

celery_app = Celery('tasks', broker=f'pyamqp://guest@{os.environ.get("RABBITMQ_HOST", "localhost")}//')
logger = get_task_logger(__name__)

@celery_app.task(name="task2")
def task2(*args, **kwargs):
    for i in range(1, 20):
        logger.info(f'----> Running task 2: Iteration {i} of 20')
        logger.info(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        sleep(2)

