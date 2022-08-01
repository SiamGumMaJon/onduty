# Generated by Django 4.0.6 on 2022-07-28 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manageduty', '0002_exception'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exception',
            options={'verbose_name_plural': 'exception : งดเวร'},
        ),
        migrations.AlterField(
            model_name='exception',
            name='detail',
            field=models.CharField(blank=True, max_length=100, verbose_name='รายละเอียดการงดเวร'),
        ),
        migrations.CreateModel(
            name='dutyhd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(blank=True, max_length=100, verbose_name='รายละเอียดการงดเวร')),
                ('edit_date', models.DateTimeField(blank=True, verbose_name='แก้ไขล่าสุด')),
                ('creat_date', models.DateTimeField(blank=True, verbose_name='สร้างเมื่อ')),
                ('dutytype_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manageduty.dutytype', verbose_name='user_id')),
                ('users_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='user_id')),
            ],
            options={
                'verbose_name_plural': 'dutyhd : ตารางเวร',
            },
        ),
    ]