# Generated by Django 2.0.2 on 2018-06-26 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0026_auto_20180622_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan_card_no', models.CharField(blank=True, max_length=20)),
                ('aadhar_card_no', models.CharField(blank=True, max_length=20)),
                ('permanent_address', models.CharField(blank=True, max_length=100)),
                ('permanent_city', models.CharField(blank=True, max_length=20)),
                ('permanent_state', models.CharField(blank=True, max_length=20)),
                ('permanent_pin', models.CharField(blank=True, max_length=20)),
                ('permanent_country', models.CharField(blank=True, max_length=20)),
                ('postal_address', models.CharField(blank=True, max_length=100)),
                ('postal_city', models.CharField(blank=True, max_length=20)),
                ('postal_state', models.CharField(blank=True, max_length=20)),
                ('postal_pin', models.CharField(blank=True, max_length=20)),
                ('postal_country', models.CharField(blank=True, max_length=20)),
                ('mobile1', models.CharField(blank=True, max_length=20)),
                ('mobile2', models.CharField(blank=True, max_length=20)),
                ('personal_email', models.CharField(blank=True, max_length=20)),
                ('office_email', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'personal_details',
            },
        ),
    ]
