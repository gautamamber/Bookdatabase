# Generated by Django 2.0.2 on 2018-06-19 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_bookdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
