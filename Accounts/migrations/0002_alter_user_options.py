# Generated by Django 4.0.3 on 2022-04-12 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'base_manager_name': 'objects', 'verbose_name': 'Member', 'verbose_name_plural': 'Members'},
        ),
    ]
