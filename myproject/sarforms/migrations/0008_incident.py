# Generated by Django 5.2.1 on 2025-05-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarforms', '0007_alter_form133next_tijd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('datum', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
