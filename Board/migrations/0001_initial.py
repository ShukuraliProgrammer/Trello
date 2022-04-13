# Generated by Django 4.0.3 on 2022-04-12 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Workspace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('visibility', models.CharField(choices=[('PR', 'Private'), ('WS', 'Workspace'), ('PB', 'Public')], default='Workspace', max_length=100, verbose_name='Visibility')),
                ('background', models.CharField(choices=[('Blue', 'Bl'), ('Orange', 'Or'), ('Green', 'Gn'), ('Red', 'Rd'), ('Purple', 'Pl'), ('Pink', 'Pk'), ('Lime', 'Lm'), ('Sky', 'Sy'), ('Gray', 'Gy')], default='Gray', max_length=100, verbose_name='Background Color')),
                ('member', models.ManyToManyField(related_name='boards', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='Workspace.workspace', verbose_name='Workspaces of Board')),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
                'order_with_respect_to': 'workspace',
            },
        ),
    ]
