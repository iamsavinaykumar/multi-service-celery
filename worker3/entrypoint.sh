#!/bin/sh

celery --app=main:celery_app worker --pool=gevent --concurrency=100 --loglevel=INFO -E -n worker_3.%h -Q queue3,queue4,queue5
