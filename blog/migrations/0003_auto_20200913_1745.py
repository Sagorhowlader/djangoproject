# Generated by Django 3.1.1 on 2020-09-13 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_context'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='context',
            new_name='content',
        ),
    ]
