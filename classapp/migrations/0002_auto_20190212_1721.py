# Generated by Django 2.0.6 on 2019-02-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmates',
            name='t_n1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='classmates',
            name='t_n2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
