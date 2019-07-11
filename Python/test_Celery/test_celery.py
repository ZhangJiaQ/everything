from __future__ import absolute_import
from celery import Celery

celery = Celery('proj',
             broker='redis',
             backend='redis://localhost:6379/0',
             include=['test_Celery.test_tasks'])
print(celery)

# Optional configuration, see the application user guide.
celery.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    celery.start()