
from django.shortcuts import render
from unahealth_app.models import GlucoseLevel, User
from django.conf import settings
import requests

def home(request):
    levels = GlucoseLevel.objects.all()
    users =  User.objects.all()
    
    # update UI: bad seperation of concerns here
    if request.GET:
        trigger_url = request.GET['trigger_url']
        if trigger_url:
            url = settings.API_URL +  trigger_url
            result = requests.get(url)
            data = result.json()
            levels = data
            print(levels)
        else:
            levels = []

    return render(request, 'index.html', {
        'levels': levels,
        'users': users
    })
