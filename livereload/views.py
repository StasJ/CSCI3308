from django.http import HttpResponse
import pathlib
import os

def index(request):
    if pathlib.Path('/tmp/reload').is_file():
        os.remove('/tmp/reload')
        return HttpResponse('1')
    else:
        return HttpResponse('0')
