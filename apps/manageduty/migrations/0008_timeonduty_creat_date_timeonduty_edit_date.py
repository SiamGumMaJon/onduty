# Generated by Django 4.0.6 on 2022-07-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageduty', '0007_timeonduty'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeonduty',
            name='creat_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='สร้างเมื่อ'),
        ),
        migrations.AddField(
            model_name='timeonduty',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='แก้ไขล่าสุด'),
        ),
    ]
