# Generated by Django 4.1.3 on 2022-12-01 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_delete_finalresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='officer',
        ),
    ]
