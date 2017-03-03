from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..loginandreg.models import User
from .models import Travel

def index(request):

    if 'id' not in request.session:
        return redirect('home:my_home')

    user= User.objects.get(id=request.session['id'])
    print Travel.objects.all()
    context={
        "user": User.objects.get(id=request.session['id']),
        "travels":Travel.objects.filter(user=user)|Travel.objects.filter(travel=user),
        "alltravels": Travel.objects.all().exclude(user=user)
    }
    return render(request, "travels/index.html", context)

def addtravel(request):
    if 'id' not in request.session:
        return redirect('home:my_home')
    return render(request, "travels/addtravel.html")

def add(request):
    if 'id' not in request.session:
        return redirect('home:my_home')
    user = User.objects.get(id=request.session['id'])
    response = Travel.objects.planreview(request.POST,user)
    if not response['Status']:
        for error in response['errors']:
            messages.error(request,error)
        return redirect("travel:add_travel")
    else:
        return redirect('travel:my_home')

def myaddtravel(request,id):
    Travel.objects.get(id=id).travel.add(User.objects.get(id=request.session['id']))
    return redirect('travel:my_home')

def destination(request,id):
    user=User.objects.get(id=request.session['id'])
    print Travel.objects.filter(id=id)
    context={
        "destination": Travel.objects.get(id=id),
        "travelers": Travel.objects.filter(id=id).exclude(user=user)
    }
    return render(request, "travels/destination.html",context)

def logout(request):
    del request.session['id']
    return redirect ('home:my_home')
