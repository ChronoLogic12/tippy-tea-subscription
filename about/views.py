from django.shortcuts import render
from django.views.defaults import server_error

# Create your views here.
def about(request):
    """ Render the about us view """
    try:
        return render(request, 'about/about.html', status=200)
    except Exception:
        return server_error(request)
