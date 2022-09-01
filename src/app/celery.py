import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.app.settings')
app = Celery('celeryApp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     return
#     sender.add_periodic_task(60.0, debug_print.s('Hola mundo'), name='add every 10')

@app.task(bind=True)
def debug_task(self):
    print(f'Solicitud: {self.request!r}')

@app.task
def debug_print(data):
    print('Debug Print ' + str(data) )
