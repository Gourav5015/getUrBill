# Generated by Django 3.2.6 on 2021-09-13 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetUrBill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_no',
            name='billpdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to='GetUrBill/media/'),
        ),
        migrations.AlterField(
            model_name='bill_no',
            name='date_of_purchase',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 13, 10, 31, 7, 303016)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=630279),
        ),
    ]
