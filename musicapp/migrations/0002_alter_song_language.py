# Generated by Django 4.0.4 on 2022-05-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='language',
            field=models.CharField(choices=[('Hindi', 'Hindi'), ('English', 'English'), ('Punjabi', 'Punjabi'), ('Haryanvi', 'Haryanvi'), ('Assamese', 'Assamese'), ('Bhojpuri', 'Bhojpuri')], default='Hindi', max_length=30),
        ),
    ]
