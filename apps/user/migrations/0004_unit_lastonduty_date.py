# Generated by Django 4.0.6 on 2022-07-29 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_users_is_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='lastonduty_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='เข้าเวรครั้งล่าสุด'),
        ),
    ]
