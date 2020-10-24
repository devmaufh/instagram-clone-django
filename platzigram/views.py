""" Platzigram views"""
#Utilities
from datetime import datetime
# Django
from django.http import HttpResponse
from django.http import JsonResponse


def hello_world( request ):
    """ Return a greeting."""
    return HttpResponse(' Server date is {now} '.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs  ')
    ))


def hi(request):
    """ Hi"""
    numbers = request.GET['numbers'].split(',')
    numbers.sort()
    return JsonResponse({'numbers': numbers})