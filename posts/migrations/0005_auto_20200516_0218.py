# Generated by Django 3.0.6 on 2020-05-16 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200516_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorter',
            name='sort_by',
            field=models.CharField(max_length=3),
        ),
    ]
