# Generated by Django 4.1.3 on 2022-12-01 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_finalresult_result_finalresult_result'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FinalResult',
        ),
    ]
