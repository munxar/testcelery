from celery import Celery

# todo: read config from settings
app = Celery('tasks', broker='django://')

# if run as script, start worker
if __name__ == '__main__':
    app.worker_main()

