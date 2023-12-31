# Generated by Django 4.2.5 on 2023-09-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='academivyear',
            new_name='academicyear',
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('CSE(Regular)', 'CSE(R)'), ('CSE(Honours)', 'CSE(H)'), ('CS&IT', 'CSIT')], max_length=100),
        ),
    ]
