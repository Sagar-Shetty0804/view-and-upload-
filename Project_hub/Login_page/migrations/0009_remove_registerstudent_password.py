# Generated by Django 5.1 on 2024-10-03 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_page', '0008_alter_registerstudent_projyear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerstudent',
            name='password',
        ),
    ]