# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-19 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashB', '0003_auto_20170619_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outwarddata',
            old_name='GLS_commission',
            new_name='BeneficiaryAmount',
        ),
        migrations.RenameField(
            model_name='outwarddata',
            old_name='amountForeign',
            new_name='BeneficiaryAmountINR',
        ),
        migrations.RenameField(
            model_name='outwarddata',
            old_name='amountINR',
            new_name='commissionAmt',
        ),
    ]
