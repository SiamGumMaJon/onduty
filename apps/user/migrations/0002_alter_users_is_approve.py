# Generated by Django 4.0.6 on 2022-07-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_approve',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]