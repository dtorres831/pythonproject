from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, "loginandreg/loginandreg.html")

def register (request):
    response = User.objects.register(request.POST)

    if not response['Status']:
        for error in response['errors']:
            messages.error(request, error)
            print response['errors']
            # print messages
        return redirect(reverse('home:my_home'))
    else:
        request.session['id']= response['user'].id
        return redirect( "travel:my_home")

def login(request):
    response = User.objects.login(request.POST)
    if not response['Status']:
        messages.error(request, response['errors'])
        return redirect(reverse('home:my_home'))
    else:
        # request.session['id']= response['user'].id
        request.session['id']= response['user'].id

        return redirect(reverse("travel:my_home"))
