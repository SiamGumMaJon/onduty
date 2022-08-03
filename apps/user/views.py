import re
from django.shortcuts import render,redirect
from .models import Users


from django.contrib.auth.views import LoginView
from .forms import MyAuthForm

def membershows(request):
    return render(request,"user/members.html")


def memberall(request):
    all_list =  Users.objects.all()
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"user/tables.html",context)

def register(request):
    return render(request,"user/register.html")

class MyLoginView(LoginView):    
    authentication_form = MyAuthForm
    template_name = 'registration/login.html'