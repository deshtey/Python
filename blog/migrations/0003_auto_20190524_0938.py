# Generated by Django 2.1.7 on 2019-05-24 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='approved',
        ),
    ]
