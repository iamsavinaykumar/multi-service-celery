import os
from celery import Celery
from celery.app.log import TaskFormatter
from celery.signals import after_setup_task_logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

celery_app = Celery('tasks', broker=f'pyamqp://guest@{os.environ.get("RABBITMQ_HOST", "localhost")}//')

app = FastAPI(title="celery_workspace")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    
    print(logger.handlers)
    for handler in logger.handlers:
        handler.setFormatter(TaskFormatter('%(asctime)s - %(task_id)s - %(task_name)s - %(name)s - %(levelname)s - %(message)s'))

@app.get('/')
def hello():
    return {
        "message": "Hello from celery_workspace"
    }

@app.get('/tasks/runall')
def run_all_tasks():
    celery_app.signature(f'task1', queue=f"queue1", args=(f'h1',), kwargs={'url': f'https://do-task-1'}).delay()
    celery_app.signature(f'task2', queue=f"queue2", args=(f'h2',), kwargs={'url': f'https://do-task-2'}).delay()
    celery_app.signature(f'task3', queue=f"queue3", args=(f'h3',), kwargs={'url': f'https://do-task-3'}).delay()
    celery_app.signature(f'task4', queue=f"queue3", args=(f'h4',), kwargs={'url': f'https://do-task-4'}).delay()
    celery_app.signature(f'task5', queue=f"queue3", args=(f'h5',), kwargs={'url': f'https://do-task-5'}).delay()
