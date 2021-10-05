import os
from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger

celery_app = Celery('tasks', broker=f'pyamqp://guest@{os.environ.get("RABBITMQ_HOST", "localhost")}//')
logger = get_task_logger(__name__)

@celery_app.task(name="task3")
def task3(*args, **kwargs):
    for i in range(1, 20):
        logger.info(f'----> Running task 3: Iteration {i} of 20')
        logger.info(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        sleep(2)

@celery_app.task(name="task4")
def task4(*args, **kwargs):
    for i in range(1, 20):
        logger.info(f'----> Running task 4: Iteration {i} of 20')
        logger.info(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        sleep(2)

@celery_app.task(name="task5")
def task5(*args, **kwargs):
    for i in range(1, 20):
        logger.info(f'----> Running task 5: Iteration {i} of 20')
        logger.info(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        sleep(2)