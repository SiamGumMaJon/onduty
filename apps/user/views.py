import re
from django.shortcuts import render,redirect
from .models import Users
from apps.manageduty.models import exception

from django.contrib.auth.views import LoginView
from .forms import MyAuthForm


class MyLoginView(LoginView):    
    authentication_form = MyAuthForm
    template_name = 'registration/login.html'


def userslist(request):
    all_list =  Users.objects.all().order_by('rank')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"user/userslist.html",context)

