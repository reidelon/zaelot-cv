# Generated by Django 3.2.6 on 2021-08-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('manager', 'manager')], default='user', max_length=120),
        ),
    ]
