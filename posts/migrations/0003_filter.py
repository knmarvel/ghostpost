# Generated by Django 3.0.6 on 2020-05-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_ghostpost_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_by', models.CharField(default='new', max_length=3)),
            ],
        ),
    ]
