# Generated by Django 4.1.2 on 2022-10-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(null=True),
        ),
    ]
