import os
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import corpora
from .filter import CorporaFilter


#the views are registrated here.
def index(request):
    # the site is only visible if the user is already logged in
    if request.user.is_authenticated:
        #the available corpora are passed true the filter
        corpora_list = corpora.objects.all()
        corporaFilter = CorporaFilter(request.GET, queryset=corpora_list)
        corpora_list = corporaFilter.qs
        #the result is given to the front end
        return render(request, 'index.html', {'corpera': corpora_list, 'corporaFilter': corporaFilter})
    #if you are not logged in, you are redirected to the login page
    else:
        return redirect('login')


def register(request):
    #if there is post message the content is collected
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #checks if password1 and 2 match
        if password == password2:
            #checks if email is already taken
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect(register)
            #checks if username is taken
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Name taken')
                return redirect('register')
            #the user is created
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

    return render(request, 'register.html')


def login(request):
    #collects content from login attempt and checks if user exists
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

#logs user out
def logout(request):
    auth.logout(request)
    return redirect('login')

#registers the corpora details site
def corporasite(request, pk):
    corporatext = corpora.objects.get(id=pk)
    return render(request, 'corpora.html', {'corpora': corporatext})


