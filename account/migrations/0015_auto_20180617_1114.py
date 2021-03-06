# Generated by Django 2.0.2 on 2018-06-17 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0014_net_amount_payable_details_royaltydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_balance', models.IntegerField(null=True)),
                ('copies_printed', models.IntegerField(null=True)),
                ('total_copies', models.IntegerField(null=True)),
                ('no_of_specimen_copies_issued', models.IntegerField(null=True)),
                ('defective_copies', models.IntegerField(null=True)),
                ('domestic_sales', models.IntegerField(null=True)),
                ('international_sales', models.IntegerField(null=True)),
                ('total_sales', models.IntegerField(null=True)),
                ('closing_stock', models.IntegerField(null=True)),
                ('royalty_rate', models.IntegerField(null=True)),
                ('royalty_amount', models.IntegerField(null=True)),
                ('total_royalty', models.FloatField(null=True)),
                ('advances', models.FloatField(null=True)),
                ('tds', models.FloatField(null=True)),
                ('net_amount_payable', models.FloatField(null=True)),
                ('payment_details', models.CharField(max_length=100)),
                ('title_name', models.CharField(max_length=30)),
                ('title_id', models.IntegerField(null=True)),
                ('title_isbn', models.CharField(max_length=20)),
                ('edition', models.CharField(max_length=20)),
                ('price', models.FloatField(null=True)),
                ('version', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='net_amount_payable_details',
            name='user',
        ),
        migrations.RemoveField(
            model_name='paymentdetails',
            name='user',
        ),
        migrations.RemoveField(
            model_name='royaltydetails',
            name='user',
        ),
        migrations.RemoveField(
            model_name='titlebook',
            name='user',
        ),
        migrations.DeleteModel(
            name='Net_amount_Payable_Details',
        ),
        migrations.DeleteModel(
            name='PaymentDetails',
        ),
        migrations.DeleteModel(
            name='RoyaltyDetails',
        ),
        migrations.DeleteModel(
            name='TitleBook',
        ),
    ]
