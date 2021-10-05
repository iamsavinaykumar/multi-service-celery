#!/bin/sh

celery --app=main:celery_app worker --pool=gevent --concurrency=100 --loglevel=INFO -E -n worker_2.%h -Q queue2
