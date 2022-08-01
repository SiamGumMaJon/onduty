from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users, Unit

@admin.register(Users)  
class UsersAdmin(UserAdmin):
    model = Users
    search_fields = ('username',"position")
    list_display = ('id','FullName', 'username','unit',  'is_active','is_staff', 'is_superuser','is_approve' ,'last_login',)
    
    list_display_links = ('FullName', 'username')
    list_filter = ('position', 'is_staff', 'is_superuser')
    list_editable =('is_active', 'is_staff', 'is_superuser','is_approve',)
    
    fieldsets = (
        (None, 
            {'fields': ('username', 'email', 'password','rank','first_name','last_name','unit','position','mobile_phone','dutytype','is_approve' )}
        ),
        ('Permissions', 
            {'fields': ('is_staff', 'is_active','is_superuser', 'groups', 'user_permissions',)}
         ),
        ('Dates', 
            {'fields': ('last_login', 'date_joined')}
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password','rank','first_name','last_name','unit','position','mobile_phone','dutytype','is_approve')}
         ),
    )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['get_unit_group_display','short_name', 'full_name','edit_date','creat_date',]
    list_display_links = ['short_name','full_name']
    search_fields = ('short_name', 'full_name')
    ordering = ["unit_group", "id"]

