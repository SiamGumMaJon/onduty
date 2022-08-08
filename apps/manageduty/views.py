from django.shortcuts import render
from .models import exception
from django.contrib.auth.decorators import login_required
from apps.user.models import Users
# Create your views here.

@login_required
def dutylist(request):
    all_list =  Users.objects.all().order_by('rank')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"manageduty/dutylist.html",context)

@login_required
def exceptionlist(request):
    # list = exception.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
    all_list =  exception.objects.all().order_by('users')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"manageduty/exceptionlist.html",context)


def dashboard(request):
    return render(request,"manageduty/dashboard.html",)

