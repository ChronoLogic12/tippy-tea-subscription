# Generated by Django 4.0.1 on 2022-07-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=10000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weight', models.CharField(max_length=50)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]
