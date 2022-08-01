import re
from django.shortcuts import render,redirect
from .models import Users


def membershows(request):
    return render(request,"user/members.html")


def memberall(request):
    all_list =  Users.objects.all()
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"user/tables.html",context)

def register(request):
    return render(request,"user/register.html")
