from django.shortcuts import render
from django.http import HttpResponse
from blog import tasks


def main(request):
    tasks.celery_tasks.delay()
    return HttpResponse("Salom")
