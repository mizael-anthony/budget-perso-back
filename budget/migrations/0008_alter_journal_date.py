# Generated by Django 3.2 on 2022-02-10 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_alter_action_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
