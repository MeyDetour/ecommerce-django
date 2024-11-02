from django.http import HttpResponseRedirect
from django.shortcuts import render

from website.forms import UserForm


def profile(request):
    if not request.user.is_authenticated:
        return  HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = UserForm()
    return  render(request, 'website/client/user/index.html',{'form':form})