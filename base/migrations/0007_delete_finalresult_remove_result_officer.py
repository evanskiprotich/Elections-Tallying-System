# Generated by Django 4.1.3 on 2022-12-01 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_finalresult_result'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FinalResult',
        ),
        migrations.RemoveField(
            model_name='result',
            name='officer',
        ),
    ]