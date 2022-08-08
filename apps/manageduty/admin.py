from django.contrib import admin
from .models import dutytype,exception,ondutylist,timeonduty

@admin.register(dutytype)
class DdutytypeAdmin(admin.ModelAdmin):
    model = dutytype
    list_display = ('duty_shortname','duty_name','edit_date','creat_date',)

@admin.register(exception)
class ExceptionAdmin(admin.ModelAdmin):
    list_display = ('users','detail','start_date','end_date',)

@admin.register(ondutylist)
class OndutylistAdmin(admin.ModelAdmin):
    list_display = ('id','users_id','start_onduty','end_onduty')

@admin.register(timeonduty)
class TimeondutyAdmin(admin.ModelAdmin):
    list_display = ('day','start_time','end_time','detail')