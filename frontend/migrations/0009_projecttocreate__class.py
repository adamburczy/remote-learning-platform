# Generated by Django 3.1.4 on 2021-01-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttocreate',
            name='_class',
            field=models.CharField(default='1B', max_length=3),
            preserve_default=False,
        ),
    ]
