"""onduty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from re import template
from django.contrib import admin 
from django.urls import path, include
from apps.user.views import userslist, MyLoginView,edit_user,delete_user
from apps.manageduty.views import dutylist,exceptionlist,officerslist,clerklist,publicrelations,dashboard
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard,name = 'dashboard'),
    path('userslist',userslist,name = 'userslist'),
    path('dutylist',dutylist,name = 'dutylist'),
    path('exceptionlist',exceptionlist,name = 'exceptionlist'),
    path('officerslist',officerslist,name = 'officerslist'),
    path('clerklist',clerklist,name = 'clerklist'),
    path('publicrelations',publicrelations,name = 'publicrelations'),
    path('account/',include('django.contrib.auth.urls')),

    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html')),

    # path('register',register,name = 'register'),
    path('login/', MyLoginView.as_view(), name = 'login'),
    # path ('member/',include('apps.user.urls'),name='member')
    path('<user_id>/edit/', edit_user, name='edit_user'),
    path('<user_id>/delete/',delete_user,name='delete_user'),
]
