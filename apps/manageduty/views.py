from django.shortcuts import render
from .models import exception
from django.contrib.auth.decorators import login_required
from apps.user.models import Users
# Create your views here. 

@login_required
def dutylist(request):
    exception_list =  exception.objects.values_list('users_id', flat=True)
    print("exception_list ",exception_list)
    all_list =  Users.objects.all().exclude(id__in = exception_list).order_by('rank')
    # Users.objects.filter(unit__name__contains = "ศูนย?..")
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"manageduty/dutylist.html",context)

@login_required
def exceptionlist(request):
    all_list =  exception.objects.all().order_by('users__rank')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"manageduty/exceptionlist.html",context)


def dashboard(request):
    return render(request,"manageduty/dashboard.html",)

