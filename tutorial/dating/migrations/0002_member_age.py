# Generated by Django 2.0.1 on 2018-03-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
    ]
