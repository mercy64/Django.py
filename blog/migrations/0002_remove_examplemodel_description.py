# Generated by Django 5.1.2 on 2024-11-05 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examplemodel',
            name='description',
        ),
    ]
