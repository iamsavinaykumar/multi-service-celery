#!/bin/sh

celery --app=main:celery_app worker --pool=gevent --concurrency=100 --loglevel=INFO -E -n worker_1.%h -Q queue1
