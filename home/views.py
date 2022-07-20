from django.shortcuts import render
from django.views.defaults import server_error

def index(request):
    """ Render homepage """
    try:
        return render(request, 'home/index.html', status=200)
    except Exception:
        return server_error(request)