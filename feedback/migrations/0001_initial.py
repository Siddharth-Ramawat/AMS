# Generated by Django 3.0.4 on 2020-03-12 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('INF', 'Infrastructure'), ('GEN', 'Generic'), ('CUR', 'Curriculum')], default='GEN', max_length=3)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('text', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]