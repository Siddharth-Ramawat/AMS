# Generated by Django 2.2.1 on 2020-03-10 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20200310_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='user_name',
            new_name='user',
        ),
    ]
