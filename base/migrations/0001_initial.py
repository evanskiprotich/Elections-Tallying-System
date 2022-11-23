# Generated by Django 4.1.3 on 2022-11-23 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate1', models.IntegerField()),
                ('candidate2', models.IntegerField()),
                ('candidate3', models.IntegerField()),
                ('candidate4', models.IntegerField()),
                ('valid_votes', models.IntegerField()),
                ('rejected_votes', models.IntegerField()),
                ('registered_voters', models.IntegerField()),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(blank=True, max_length=30)),
                ('county_code', models.IntegerField()),
                ('constituency', models.CharField(blank=True, max_length=30)),
                ('constituency_code', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]