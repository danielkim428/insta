# Generated by Django 3.0.3 on 2020-12-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('content', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
