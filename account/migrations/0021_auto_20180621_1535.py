# Generated by Django 2.0.2 on 2018-06-21 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20180619_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personal_details',
            name='user',
        ),
        migrations.DeleteModel(
            name='BookData',
        ),
        migrations.DeleteModel(
            name='Personal_details',
        ),
    ]
