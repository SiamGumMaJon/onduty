from django.db import models




class dutytype(models.Model):
    duty_shortname = models.CharField(verbose_name="หน้าที่เวร",max_length=50)
    duty_name = models.CharField(verbose_name="หน้าที่เวร",max_length=200)
    detail = models.CharField(verbose_name="รายละเอียดหน้าที่เวร",max_length=100,blank = True )
    edit_date = models.DateTimeField(verbose_name="แก้ไขล่าสุด",blank = True )
    creat_date = models.DateTimeField(verbose_name="สร้างเมื่อ",blank = True)
    class Meta:
        verbose_name_plural = "Duty : ประเภทการเข้าเวร" 
        
    def __str__(self):
        return f'{self.duty_shortname}'


class exception(models.Model):
    users = models.ForeignKey("user.Users", verbose_name='user_id', on_delete=models.DO_NOTHING, null= True, blank=True)
    detail = models.CharField(verbose_name="รายละเอียดการงดเวร",max_length=100,null = True ,blank = True )
    start_date = models.DateTimeField(verbose_name="เริ่ม",null = True ,blank = True )
    end_date = models.DateTimeField(verbose_name="สิ้นสุด",null = True ,blank = True)
    edit_date = models.DateTimeField(verbose_name="แก้ไขล่าสุด",null = True ,blank = True )
    creat_date = models.DateTimeField(verbose_name="สร้างเมื่อ",null = True ,blank = True) 
    
    class Meta:
        verbose_name_plural = "exception : งดเวร"

    def __str__(self):
        return f'{self.users_id}'
 

# class dutyhd(models.Model):
#     dutytype_id = models.ForeignKey(dutytype, verbose_name='user_id', on_delete=models.DO_NOTHING, null= True, blank=True)
#     period = models.DateField(verbose_name="เวรประจำเดือน",max_length=100,blank = True )
#     edit_date = models.DateTimeField(verbose_name="แก้ไขล่าสุด",blank = True )
#     creat_date = models.DateTimeField(verbose_name="สร้างเมื่อ",blank = True) 
    
#     class Meta:
#         verbose_name_plural = "dutyhd : ตารางเวร"

#     def __str__(self):
#         return f'ประเภทเวร {self.dutytype_id} ของเดือน {self.period}'
 

class ondutylist(models.Model):
    users = models.ForeignKey("user.Users", verbose_name='user_id', on_delete=models.DO_NOTHING, null= True, blank=True)
    start_onduty =models.DateTimeField(verbose_name="วัน-เวลา เริ่มเข้าเวร",null = True ,blank = True )
    end_onduty =models.DateTimeField(verbose_name="วัน-เวลา สิ้นสุด",null = True ,blank = True )
    edit_date = models.DateTimeField(verbose_name="แก้ไขล่าสุด",null = True ,blank = True )
    creat_date = models.DateTimeField(verbose_name="สร้างเมื่อ",null = True ,blank = True) 
    
    class Meta:
        verbose_name_plural = "dutyhd : ตารางเวร"

    def __str__(self):
        return f'ประเภทเวร {self.users_id} ของเดือน {self.start_onduty}'

class timeonduty(models.Model):
    day = models.DateTimeField(verbose_name="สร้างเมื่อ",null = True ,blank = True) 
    start_time = models.DateTimeField(verbose_name="สร้างเมื่อ",null = True ,blank = True) 
    end_time = models.DateTimeField(verbose_name="สร้างเมื่อ",null = True ,blank = True)
    detail = models.CharField(verbose_name="รายละเอียดการงดเวร",max_length=100,null = True ,blank = True )
    edit_date = models.DateTimeField(verbose_name="แก้ไขล่าสุด",null = True ,blank = True )
    creat_date = models.DateTimeField(verbose_name="สร้างเมื่อ",null = True ,blank = True) 

    class Meta:
        verbose_name_plural = "timeonduty : วัน-เวลา เข้าเวร"

    def __str__(self):
        return f' {self.day} '