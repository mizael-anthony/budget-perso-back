# Generated by Django 3.2 on 2022-02-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20220204_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='logo',
            field=models.FileField(default='img/unknown.png', upload_to='img/'),
        ),
    ]
