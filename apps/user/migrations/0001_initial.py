# Generated by Django 4.0.6 on 2022-08-04 04:31

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('manageduty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_group', models.CharField(choices=[('0', '-'), ('1', 'ส่วนบังคับบัญชา'), ('2', 'กองทัพอากาศ (กองบัญชาการ)'), ('3', 'ส่วนบัญชาการ'), ('4', 'ส่วนกำลังรบ'), ('5', 'ส่วนส่งกำลังบำรุง'), ('6', 'ส่วนการศึกษา'), ('7', 'ส่วนกิจการพิเศษ')], default=None, max_length=1)),
                ('short_name', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=90)),
                ('edit_date', models.DateTimeField(null=True, verbose_name='แก้ไขล่าสุด')),
                ('creat_date', models.DateTimeField(null=True, verbose_name='สร้างเมื่อ')),
            ],
            options={
                'verbose_name_plural': 'Unit : หน่วยขึ้นตรง ทอ.',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rank', models.PositiveIntegerField(blank=True, choices=[(30101, 'พล.อ.อ.*'), (30102, 'พล.อ.อ.*หญิง'), (30211, 'พล.อ.อ.'), (30212, 'พล.อ.อ.หญิง'), (30213, 'พล.อ.'), (30221, 'พล.อ.ท.'), (30222, 'พล.อ.ท.หญิง'), (30231, 'พล.อ.ต.'), (30232, 'พล.อ.ต.หญิง'), (30301, 'น.อ.(พ)'), (30302, 'น.อ.(พ) หญิง'), (30410, 'พ.อ.'), (30411, 'น.อ.'), (30412, 'น.อ.หญิง'), (30420, 'พ.ท.'), (30421, 'น.ท.'), (30422, 'น.ท.หญิง'), (30431, 'น.ต.'), (30432, 'น.ต.หญิง'), (30511, 'ร.อ.'), (30512, 'ร.อ.หญิง'), (30521, 'ร.ท.'), (30522, 'ร.ท.หญิง'), (30531, 'ร.ต.'), (30532, 'ร.ต.หญิง'), (30541, 'กห.ส.'), (30542, 'กห.ส.หญิง'), (30611, 'พ.อ.อ.(พ)'), (30612, 'พ.อ.อ.(พ) หญิง'), (30711, 'พ.อ.อ.'), (30712, 'พ.อ.อ.หญิง'), (30721, 'พ.อ.ท.'), (30722, 'พ.อ.ท.หญิง'), (30731, 'พ.อ.ต.'), (30732, 'พ.อ.ต.หญิง'), (30811, 'จ.อ.'), (30812, 'จ.อ.หญิง'), (30821, 'จ.ท.'), (30822, 'จ.ท.หญิง'), (30831, 'จ.ต.'), (30832, 'จ.ต.หญิง'), (30841, 'กห.ป.'), (30842, 'กห.ป.หญิง'), (39200, 'พนง.อาวุโสหญิง'), (39201, 'พนง.อาวุโส'), (39400, 'พนง.หญิง'), (39401, 'พนง.'), (39600, 'นาย'), (39601, 'นาง'), (39602, 'น.ส.'), (0, '')], default=0, null=True, verbose_name='ยศ')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='ตำแหน่ง')),
                ('mobile_phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='เบอร์มือถือ')),
                ('is_approve', models.BooleanField(blank=True, null=True)),
                ('dutytype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manageduty.dutytype', verbose_name='ประเภทเวร')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_unit', to='user.unit', verbose_name='สังกัด')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'User : ผู้ใช้ระบบ',
                'permissions': (('UNIT_REQUESTER', 'UNIT_Requester'), ('UNIT_ADMIN', 'Unit_Admin'), ('UNIT_COMMANDER', 'Unit_Commander'), ('SCIENCE_ADMIN', 'Science_Admin'), ('PERSON_ADMIN', 'Person_admin')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
