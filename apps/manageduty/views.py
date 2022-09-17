from django.shortcuts import render
from .models import exception,ondutylist
from django.contrib.auth.decorators import login_required
from apps.user.models import Users
# Create your views here. 


@login_required
def dutylist(request):
    exception_list =  exception.objects.all()
    # print("exception_list ",exception_list)

    ondutylist_detail = ondutylist.objects.all()
    # print("ondutylist_detail",ondutylist_detail)


    # all_list =  Users.objects.all().exclude(id__in = exception_list).order_by('rank')
    all_list =  Users.objects.all().order_by('rank')
    # Users.objects.filter(unit__name__contains = "ศูนย?..")
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist, "exception_list_data": exception_list , "ondutylist_detail_data":ondutylist_detail}
    print (context)
    return render(request,"manageduty/dutylist.html",context)

@login_required
def exceptionlist(request):
    all_list =  exception.objects.all().order_by('users__rank')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"manageduty/exceptionlist.html",context)

@login_required
def officerslist(request):
    exception_list =  exception.objects.all()
    # print("exception_list ",exception_list)

    ondutylist_detail = ondutylist.objects.all()
    # print("ondutylist_detail",ondutylist_detail)

    # all_list =  Users.objects.all().exclude(id__in = exception_list).order_by('rank')
    all_list =  Users.objects.filter(dutytype=1).order_by('rank')
    # Users.objects.filter(unit__name__contains = "ศูนย?..")
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist, "exception_list_data": exception_list , "ondutylist_detail_data":ondutylist_detail}
    print (context)
    return render(request,"manageduty/dutylist.html",context)


@login_required
def clerklist(request):
    exception_list =  exception.objects.all()
    # print("exception_list ",exception_list)

    ondutylist_detail = ondutylist.objects.all()
    # print("ondutylist_detail",ondutylist_detail)

    # all_list =  Users.objects.all().exclude(id__in = exception_list).order_by('rank')
    all_list =  Users.objects.filter(dutytype=2).order_by('rank')
    # Users.objects.filter(unit__name__contains = "ศูนย?..")
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist, "exception_list_data": exception_list , "ondutylist_detail_data":ondutylist_detail}
    print (context)
    return render(request,"manageduty/dutylist.html",context)

@login_required
def publicrelations(request):
    exception_list =  exception.objects.all()
    # print("exception_list ",exception_list)

    ondutylist_detail = ondutylist.objects.all()
    # print("ondutylist_detail",ondutylist_detail)

    # all_list =  Users.objects.all().exclude(id__in = exception_list).order_by('rank')
    all_list =  Users.objects.filter(dutytype=3).order_by('rank')
    # Users.objects.filter(unit__name__contains = "ศูนย?..")
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist, "exception_list_data": exception_list , "ondutylist_detail_data":ondutylist_detail}
    print (context)
    return render(request,"manageduty/dutylist.html",context)



def dashboard(request):
    exception_list =  exception.objects.all()
    count_exception_list = exception_list.count()
    
    ondutylist_list = ondutylist.objects.all()
    count_ondutylist_list = ondutylist_list.count()

    all_list =  Users.objects.all()
    count_all_list = all_list.count()

    dutytype1 =  Users.objects.filter(dutytype=1)
    dutytype2 =  Users.objects.filter(dutytype=2)
    dutytype3 =  Users.objects.filter(dutytype=3)
    dutytype4 =  Users.objects.filter(dutytype=4)

    count_dutytype1 = dutytype1.count()
    count_dutytype2 = dutytype2.count()
    count_dutytype3 = dutytype3.count()
    count_dutytype4 = dutytype4.count()

    context = { 

        "count_dutytype1" : count_dutytype1,
        "count_dutytype2" : count_dutytype2,
        "count_dutytype3" : count_dutytype3,
        "count_dutytype4" : count_dutytype4,
        "count_all_list" :  count_all_list, 
        "count_exception_list": count_exception_list , 
        "count_ondutylist_list":count_ondutylist_list
        
        
        }

    # print (context)
    return render(request,"manageduty/dashboard.html",context)

