# Generated by Django 5.1.3 on 2024-11-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DEPNAME', models.CharField(max_length=100)),
            ],
        ),
    ]