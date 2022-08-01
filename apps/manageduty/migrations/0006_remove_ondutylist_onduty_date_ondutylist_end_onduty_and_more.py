# Generated by Django 4.0.6 on 2022-07-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageduty', '0005_ondutylist_delete_dutyhd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ondutylist',
            name='onduty_date',
        ),
        migrations.AddField(
            model_name='ondutylist',
            name='end_onduty',
            field=models.DateTimeField(blank=True, null=True, verbose_name='วัน-เวลา สิ้นสุด'),
        ),
        migrations.AddField(
            model_name='ondutylist',
            name='start_onduty',
            field=models.DateTimeField(blank=True, null=True, verbose_name='วัน-เวลา เริ่มเข้าเวร'),
        ),
        migrations.AlterField(
            model_name='exception',
            name='creat_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='สร้างเมื่อ'),
        ),
        migrations.AlterField(
            model_name='exception',
            name='detail',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='รายละเอียดการงดเวร'),
        ),
        migrations.AlterField(
            model_name='exception',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='แก้ไขล่าสุด'),
        ),
        migrations.AlterField(
            model_name='exception',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='สิ้นสุด'),
        ),
        migrations.AlterField(
            model_name='exception',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='เริ่ม'),
        ),
        migrations.AlterField(
            model_name='ondutylist',
            name='creat_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='สร้างเมื่อ'),
        ),
        migrations.AlterField(
            model_name='ondutylist',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='แก้ไขล่าสุด'),
        ),
    ]