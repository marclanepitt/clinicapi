# Generated by Django 2.0.3 on 2018-08-09 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinics', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.Sport'),
        ),
    ]