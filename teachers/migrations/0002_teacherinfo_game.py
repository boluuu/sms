# Generated by Django 2.2.2 on 2021-02-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherinfo',
            name='game',
            field=models.TextField(blank=True, null=True),
        ),
    ]
