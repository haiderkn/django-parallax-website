from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

from .models import BlogModel

from .forms import PostBlogForm

import time

# Create your views here.

def loginForm(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data['username']
            userp = frm.cleaned_data['password']
            user = authenticate(username =usern, password=userp)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/blog/post')
    else:
        frm = AuthenticationForm()
        blogs = BlogModel.objects.all()
        return render(request, 'blog/myblog.html', {'form': frm, 'blog':blogs})
    


def postblogView(request):
    if request.method == "POST":
        frm = PostBlogForm(request.POST)
        if frm.is_valid():
            idate = frm.cleaned_data['date']
            iwriter = frm.cleaned_data['writer']
            ititle = frm.cleaned_data['title']
            iblog = frm.cleaned_data['blog']
            data = BlogModel(date = idate,writer = iwriter, title = ititle, blog = iblog)
            data.save()
    else:
        frm = PostBlogForm()
    return render(request, 'blog/postblog.html', {'form':frm})



