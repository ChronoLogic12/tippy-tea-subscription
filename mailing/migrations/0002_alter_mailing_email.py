# Generated by Django 4.0.1 on 2022-07-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]