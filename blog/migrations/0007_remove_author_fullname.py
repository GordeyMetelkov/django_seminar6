# Generated by Django 5.0.3 on 2024-03-25 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_author_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='fullname',
        ),
    ]