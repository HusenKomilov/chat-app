from celery import shared_task
from time import sleep
import logging

logger = logging.getLogger(__name__)

@shared_task()
def celery_tasks():
    logger.info("FOUND EDITION")
    sleep(20)
    print("test")
    logger.info("FOUND EDITION")

