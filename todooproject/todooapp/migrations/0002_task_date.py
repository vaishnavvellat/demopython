# Generated by Django 4.1.7 on 2023-04-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todooapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-12-14'),
            preserve_default=False,
        ),
    ]
