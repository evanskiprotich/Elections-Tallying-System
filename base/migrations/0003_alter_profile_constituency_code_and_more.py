# Generated by Django 4.1.3 on 2022-11-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='constituency_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='county_code',
            field=models.IntegerField(null=True),
        ),
    ]
