# Generated by Django 4.1 on 2022-09-21 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depname', models.CharField(max_length=50)),
                ('depdes', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=50)),
                ('depname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pemail', models.EmailField(max_length=254)),
                ('pdate', models.DateField()),
                ('bdate', models.DateField(auto_now=True)),
                ('dname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctor')),
            ],
        ),
    ]
