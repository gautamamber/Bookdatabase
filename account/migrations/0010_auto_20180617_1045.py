# Generated by Django 2.0.2 on 2018-06-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_net_amount_payable_details_paymentdetails_royaltydetails_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='payment_details',
            field=models.IntegerField(),
        ),
    ]
