# multi-service-celery
Run celery in distributed mode

## Startup

```shell
$ docker-compose up -d 
```

## Endpoints

- `http://localhost:8000/` *[GET]* -> Hello World   
- `http://localhost:8000/tasks/runall` *[GET]* -> Run all configured tasks in their respective queue

#TODO

- endpoint for workers and monitors to request celery config from the producer 
- monitor should receive metadata for the event (anyway possible)
