# Generated by Django 2.2.2 on 2021-02-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20210207_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinfo',
            name='class_held',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
