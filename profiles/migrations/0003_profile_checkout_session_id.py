# Generated by Django 4.0.1 on 2022-07-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_mailing'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='checkout_session_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
