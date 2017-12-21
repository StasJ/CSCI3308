from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from shutil import copyfile
from django.conf import settings
from os.path import expanduser

def resetView(request):
    copyfile(expanduser("~") + "/db.sqlite3", settings.BASE_DIR + "/db.sqlite3")
    return HttpResponse('The database has been reset. <a href="/">Return to landing page</a>')
