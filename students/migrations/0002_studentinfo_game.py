# Generated by Django 2.2.2 on 2021-02-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='game',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
