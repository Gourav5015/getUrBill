# Generated by Django 3.2.6 on 2021-09-14 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetUrBill', '0002_auto_20210913_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='GST',
        ),
        migrations.AlterField(
            model_name='bill_no',
            name='date_of_purchase',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 14, 17, 20, 50, 96194)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=669280),
        ),
    ]
