from django.test import TestCase
from django.http import HttpResponse


def muni(request):
    return HttpResponse("hello , my name is munikrishana")


    # Create your tests here.
