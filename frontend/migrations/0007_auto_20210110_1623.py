# Generated by Django 3.1.4 on 2021-01-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20210109_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttocreate',
            name='your_name',
        ),
        migrations.RemoveField(
            model_name='projecttoupload',
            name='notes',
        ),
        migrations.AlterField(
            model_name='projecttocreate',
            name='teacher',
            field=models.CharField(max_length=30),
        ),
    ]
