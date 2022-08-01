from django.shortcuts import render
from .models import member
# Create your views here.


def showmember(request):
    all_list =  member.objects.all().order_by('-id')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request, "manageduty/showduty.html", context)