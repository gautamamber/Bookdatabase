# Generated by Django 2.0.2 on 2018-06-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20180617_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='closing_stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='international_sales',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='royalty_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='royalty_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='total_sales',
            field=models.IntegerField(null=True),
        ),
    ]
