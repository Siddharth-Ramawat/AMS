# Generated by Django 2.2.1 on 2020-03-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
