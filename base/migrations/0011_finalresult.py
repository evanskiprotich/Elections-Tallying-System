# Generated by Django 4.1.3 on 2022-12-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_delete_finalresult_result_officer'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ManyToManyField(to='base.result')),
            ],
        ),
    ]
