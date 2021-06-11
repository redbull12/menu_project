# Generated by Django 3.1 on 2021-06-11 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dish_app', '0002_auto_20210610_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MenuForWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.CharField(max_length=200)),
                ('lunch', models.CharField(max_length=200)),
                ('dinner', models.CharField(max_length=200)),
                ('day_of_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='dish_app.dayofweek')),
            ],
        ),
    ]
