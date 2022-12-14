# Generated by Django 3.2 on 2022-02-01 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('category', models.CharField(choices=[('charge', 'Charge'), ('produit', 'Produit')], max_length=20)),
                ('logo', models.FileField(null=True, unique=True, upload_to='img/')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('cost', models.IntegerField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.action')),
            ],
        ),
    ]
