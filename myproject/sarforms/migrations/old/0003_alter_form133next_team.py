# Generated by Django 5.2 on 2025-05-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarforms', '0002_form133next'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form133next',
            name='team',
            field=models.CharField(),
        ),
    ]
