# Generated by Django 4.1.3 on 2022-12-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_delete_finalresult_remove_result_officer'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
