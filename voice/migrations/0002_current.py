# Generated by Django 3.0.3 on 2020-12-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
            ],
        ),
    ]