
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from website.forms import  LoginForm


def register_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'website/client/registration/login.html',
                              {'form': form, 'formName': 'register', 'error': 'Name already exist'})
            user = User.objects.create_user(username= form.cleaned_data.get('username'), password=  form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'website/client/registration/login.html', {'form':form,'formName':'register','error':''})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user =authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is None:
                return render(request, 'website/client/registration/login.html',
                              {'form': form, 'formName': 'login', 'error': 'No user'})
            login(request, user)
            return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'website/client/registration/login.html', {'form':form,'formName':'login','error':''})