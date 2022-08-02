import re
from uuid import RESERVED_FUTURE


from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import RTAFUnitSection, CHOICE_Rank, USER_PERMISSION


class Unit(models.Model):
    unit_group = models.CharField(max_length = 1, default = None, choices = RTAFUnitSection.choices)        
    short_name = models.CharField(max_length = 20, blank = False)
    full_name  = models.CharField(max_length = 90, blank = False)
    edit_date = models.DateTimeField(verbose_name="แก้ไขล่าสุด",null= True)
    creat_date = models.DateTimeField(verbose_name="สร้างเมื่อ",null= True)

    class Meta:
        verbose_name_plural = "Unit : หน่วยขึ้นตรง ทอ." 
        
    def __str__(self):
        return f'{self.short_name}'

class Users(AbstractUser):
    rank = models.PositiveIntegerField(verbose_name="ยศ", choices = CHOICE_Rank, default = 0, null=True, blank=True)
    unit = models.ForeignKey(Unit, verbose_name="สังกัด", on_delete=models.SET_NULL, null=True, blank=True, related_name='current_unit')
    position = models.CharField(verbose_name="ตำแหน่ง", max_length=100,null=True, blank=True)
    mobile_phone = models.CharField(verbose_name="เบอร์มือถือ",max_length=30, null=True, blank=True)
    dutytype = models.ForeignKey("manageduty.dutytype", verbose_name='ประเภทเวร', on_delete=models.DO_NOTHING, null=True, blank=True)
    is_approve = models.BooleanField(null=True, blank=True)

    # def unit_name(self):
    #     return f"{self.get_unit_id_display()}"
    def unit_name(self):
        return f'{self.unit}'


    def dutytype_name (self):
        return f'{self.dutytype}'

    def full_name(self):
        return f"{self.rank_display()} {self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "User : ผู้ใช้ระบบ" 
        permissions = USER_PERMISSION

    def rank_display(self):
        RankDisplay = str(self.get_rank_display())
        if RankDisplay == '':
            return  ''
                        
        if "ว่าที่" in RankDisplay:
            RankDisplay = RankDisplay[6:]
        elif "กห." in RankDisplay:
            if "หญิง" in RankDisplay:
                RankDisplay = "น.ส."
            else:
                RankDisplay = "นาย"
        elif "พนง." in RankDisplay:
            if "หญิง" in RankDisplay:
                RankDisplay = "น.ส."
            else:
                RankDisplay = "นาย"

        if re.findall("หญิง", RankDisplay ):
            return f'{RankDisplay} '        
        elif re.findall("(พ)", RankDisplay ):
            RankDisplay = RankDisplay.replace("(พ)", "")    
        
        return f'{RankDisplay}'
        
    @property
    def FullName(self):        
        return f'{self.rank_display()}{self.first_name} {self.last_name}'

    def __str__(self):
        return self.FullName

