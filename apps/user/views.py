import re
from django.shortcuts import render,redirect
from .models import Users
from apps.manageduty.models import exception
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import MyAuthForm,UsersForm
from django.contrib import messages


class MyLoginView(LoginView):    
    authentication_form = MyAuthForm
    template_name = 'registration/login.html'

@login_required
def userslist(request):
    all_list =  Users.objects.all().order_by('rank')
    countlist = all_list.count()
    context = {"all_data" : all_list, "num_task" : countlist}
    return render(request,"user/userslist.html",context)

@login_required
def delete_user(request, user_id):
    userdata = Users.objects.get(id = user_id)
    deletd_name = Users.FullName
    userdata.delete()
    messages.info(request, f'ลบรายการ สำเร็จ')
    # messages.info(request, f'ลบรายการ { deletd_name } สำเร็จ')
    return redirect('/userslist')

@login_required
def edit_user(request, user_id):
    userdata = Users.objects.get(id = user_id)
    if request.method == "POST":
        my_new_data = UsersForm(request.POST,  instance = userdata)
        if my_new_data.is_valid() :
            my_new_data.save()
            return redirect('/userslist')

    my_form = UsersForm(instance = userdata)
    context = {"form" : my_form}
    return render(request,'user/edit_user.html', context)        