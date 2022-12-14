# Generated by Django 4.1.3 on 2022-11-29 18:03

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
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(blank=True, max_length=30)),
                ('candidate_image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('candidate_party', models.CharField(blank=True, max_length=60)),
                ('party_logo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(blank=True, max_length=30)),
                ('county_code', models.IntegerField(null=True)),
                ('constituency', models.CharField(blank=True, max_length=30)),
                ('constituency_code', models.IntegerField(null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Officer')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ElectionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_one', models.IntegerField(blank=True, null=True)),
                ('candidate_two', models.IntegerField(blank=True, null=True)),
                ('candidate_three', models.IntegerField(blank=True, null=True)),
                ('candidate_four', models.IntegerField(blank=True, null=True)),
                ('totalvotes', models.IntegerField(blank=True, null=True)),
                ('rejectedvotes', models.IntegerField(blank=True, null=True)),
                ('validvotes', models.IntegerField(blank=True, null=True)),
                ('regvoters', models.IntegerField(blank=True, null=True)),
                ('officer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
