# Generated by Django 2.2.2 on 2021-02-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentinfo_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='student_number',
            field=models.CharField(max_length=8),
        ),
    ]
