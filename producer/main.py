import os
from typing import List
from celery import Celery, current_app
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

registered_tasks = {}

@app.on_event("startup")
async def startup_event():
    global registered_tasks
    i = celery_app.control.inspect()
    registered_tasks = i.registered()

@app.get('/')
def hello():
    return {
        "message": "Hello from celery_workspace"
    }
@celery_app.task
@app.get('/tasks/runall')
def run_all_tasks():
    celery_app.signature(f'task1', queue=f"queue1", args=(f'h1',), kwargs={'url': f'https://do-task-1'}).delay()
    celery_app.signature(f'task2', queue=f"queue2", args=(f'h2',), kwargs={'url': f'https://do-task-2'}).delay()
    celery_app.signature(f'task3', queue=f"queue3", args=(f'h3',), kwargs={'url': f'https://do-task-3'}).delay()
    celery_app.signature(f'task4', queue=f"queue3", args=(f'h4',), kwargs={'url': f'https://do-task-4'}).delay()
    celery_app.signature(f'task5', queue=f"queue3", args=(f'h5',), kwargs={'url': f'https://do-task-5'}).delay()
    return {
        "status": "success"
    }

@app.get('/tasks/get-registered')
def get_all_registered_tasks():
    # Inspect all nodes.
    i = celery_app.control.inspect()

    # Show the items that have an ETA or are scheduled for later processing
    print(i.scheduled())

    # Show tasks that are currently active.
    print(i.active())

    # Show tasks that have been claimed by workers
    print(i.reserved())

    # Show tasks that have been claimed by workers
    print(i.registered())

    print(i)
    
    return {
        "registered_tasks": i.registered()
    }