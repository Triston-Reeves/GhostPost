# Generated by Django 3.1 on 2020-08-19 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GhostTown', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastroast',
            name='timeposted',
        ),
        migrations.AddField(
            model_name='boastroast',
            name='choices',
            field=models.BooleanField(choices=[(True, 'Boast'), (False, 'Roast')], default=True),
        ),
        migrations.AddField(
            model_name='boastroast',
            name='time_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='boastroast',
            name='user_input',
            field=models.CharField(default='', max_length=280),
        ),
    ]