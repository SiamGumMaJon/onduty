from django.shortcuts import render
from .models import exception

from apps.user.models import Users
# Create your views here.


def dutylist(request):
    all_list =  Users.objects.all().order_by('rank')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"manageduty/dutylist.html",context)


def exceptionlist(request):
    all_list =  exception.objects.all()
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"manageduty/exceptionlist.html",context)    